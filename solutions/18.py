from __future__ import annotations

import json
from functools import reduce
from itertools import permutations
from math import ceil, floor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    nested_list: TypeAlias = int | list['nested_list']
    flat_list: TypeAlias = list[tuple[int, int]]
    line_type: TypeAlias = flat_list


def line_parse(line: str) -> line_type:
    lst = json.loads(line.strip())
    return parse_nested(lst, 0)


def find_explosion(number: flat_list) -> int | None:
    """Return index of pending explosion else None"""
    for i, (_, l) in enumerate(number):
        if l == 5:
            return i


def find_split(number: flat_list) -> int | None:
    """Return index of pending split else None"""
    for i, (v, _) in enumerate(number):
        if v > 9:
            return i


def explode(number: flat_list) -> int | None:
    """Explode pair if it exists, return index of explosion or None

    Removes the left element and sets right element to (0, 4)
    Propagates values to left and right nodes if they exist.
    """
    pos = find_explosion(number)
    if pos is None:
        return

    left_val, _ = number.pop(pos)
    right_val, _ = number[pos]
    number[pos] = (0, 4)

    n = len(number)
    for dx, val in [(pos - 1, left_val), (pos + 1, right_val)]:
        if 0 <= dx < n:
            v, l = number[dx]
            number[dx] = (v + val, l)

    return pos


def split(number: flat_list) -> int | None:
    """Split node if it exists, return index of split or None

    Replace node with right split and inserts left split
    """
    pos = find_split(number)
    if pos is None:
        return

    val, level = number[pos]
    new_val = val / 2
    level += 1
    number[pos] = (ceil(new_val), level)
    number.insert(pos, (floor(new_val), level))

    return pos


def reduce_number(number: flat_list):
    """Fully reduce number

    Apply explosion-split cycle until number is fully reduced
    """
    while True:
        if explode(number) is not None:
            continue
        if split(number) is None:
            break


def add(left: flat_list, right: flat_list) -> flat_list:
    """Return added number, fully reduced"""
    number = [(v, l + 1) for v, l in left + right]
    reduce_number(number)
    return number


def parse_nested(lst: nested_list, level: int) -> flat_list:
    """Return flat representation of nested list structure"""
    if isinstance(lst, int):
        return [(lst, level)]
    return [number for el in lst for number in parse_nested(el, level + 1)]


def level_magnitude(number: flat_list, level: int) -> flat_list:
    """Return numbers with all pairs at depth `level` reduced"""
    stack = []
    for el_val, el_level in number:
        if stack and stack[-1][1] == el_level == level:
            left_val, level = stack.pop()
            el_val = left_val * 3 + el_val * 2
            el_level = level - 1

        stack.append((el_val, el_level))

    return stack


def magnitude(number: flat_list) -> int:
    """Return magnitude of number

    Eliminate each level, starting at the innermost level.
    """
    deepest = max(l for _, l in number)
    for i in range(deepest, 0, -1):
        number = level_magnitude(number, i)
    return number[0][0]


def solution(numbers: list[line_type]) -> solution_tuple:
    """
    Restructure the data into a flat list where each element
    encodes both its value and depth in the structure. This makes
    the reductions simple to implement, although there is some
    performance loss from poping and inserting elements.
    """
    sol1 = magnitude(reduce(add, numbers))

    pairs = permutations(range(len(numbers)), 2)
    sol2 = max(magnitude(add(numbers[i], numbers[j])) for i, j in pairs)
    return sol1, sol2

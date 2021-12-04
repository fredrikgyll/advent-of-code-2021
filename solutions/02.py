from __future__ import annotations

from itertools import accumulate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    line_type: TypeAlias = tuple[int, int]


def line_parse(line: str) -> line_type:
    d, val = line.strip().split(' ')
    val = int(val)
    if d == 'forward':
        return (0, val)
    elif d == 'down':
        return (val, 0)
    else:
        return (-val, 0)


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    dep, hor = list(zip(*puzzle_input))
    sol1 = sum(dep) * sum(hor)

    cum_aim = list(accumulate(dep))
    dep_inc = [a * x for x, a in zip(hor, cum_aim) if x]
    hor = sum(hor)
    dep = sum(dep_inc)
    sol2 = hor * dep

    return sol1, sol2

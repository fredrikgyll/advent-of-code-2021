from __future__ import annotations

from statistics import mean, median
from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import Callable, TypeAlias

    from solutions.utils import solution_tuple

    line_type: TypeAlias = list[int]


def dist(x: int, y: int) -> int:
    return abs(x - y)


def triangle_dist(x: int, y: int) -> int:
    n = dist(x, y)
    return (n * (n + 1)) // 2


def fuel(dist_f: Callable[[int, int], int], numbers: list[int], value: int) -> int:
    return sum(dist_f(c, value) for c in numbers)


def line_parse(line: str) -> line_type:
    return ints(line, split=',')


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    crabs = puzzle_input[0]
    middle_1 = int(median(crabs))
    middle_2 = int(mean(crabs))

    sol1 = fuel(dist, crabs, middle_1)
    sol2 = fuel(triangle_dist, crabs, middle_2)
    return sol1, sol2

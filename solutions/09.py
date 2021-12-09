from __future__ import annotations

import operator
from functools import reduce
from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import Sequence, TypeAlias

    from solutions.utils import solution_tuple

    line_type: TypeAlias = list[int]


def safe_get(lst: Sequence[int], i: int, fill: int = 99) -> int:
    if i < 0 or i >= len(lst):
        return fill
    return lst[i]


def safe_get_2d(lst: Sequence[Sequence[int]], i: int, j: int, fill: int = -1) -> int:
    if i < 0 or i >= len(lst):
        return fill
    row = lst[i]
    if j < 0 or j >= len(row):
        return fill
    return row[j]


def mins(lst: Sequence[int]) -> list[bool]:
    """Return list of bools indicating if element is local minimum"""
    return [safe_get(lst, i - 1) > el < safe_get(lst, i + 1) for i, el in enumerate(lst)]


def basin_size(grid: list[list[int]], start: tuple[int, int]) -> int:
    """BFS from minimum, counting visits"""
    i, j = start
    seen = {(i, j, safe_get_2d(grid, i, j))}
    visited = set()
    basin = 0
    while seen:
        at = seen.pop()
        i, j, h = at
        visited.add(at)
        basin += 1
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            nh = safe_get_2d(grid, ni, nj)
            np = (ni, nj, nh)
            if np not in visited and nh > h and nh != 9:
                seen.add(np)
    return basin


def line_parse(line: str) -> line_type:
    return ints(list(line.strip()))


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    """
    Find local minimums row-wise and column-wise and zip the results together
    to find the minimums in 2 dimensions.

    Use BFS to find the size of the basins
    """
    rows = [mins(l) for l in puzzle_input]
    cols = zip(*[mins(l) for l in zip(*puzzle_input)])
    points = [
        (i, j) for i, (r, c) in enumerate(zip(rows, cols)) for j, (x, y) in enumerate(zip(r, c)) if x and y
    ]

    sol1 = sum(puzzle_input[r][c] + 1 for r, c in points)

    basins = sorted([basin_size(puzzle_input, p) for p in points], reverse=True)
    sol2 = reduce(operator.mul, basins[:3])
    return sol1, sol2

from __future__ import annotations

from itertools import product
from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    grid: TypeAlias = list[list[int]]
    line_type: TypeAlias = list[int]


def line_parse(line: str) -> line_type:
    return ints(line.strip(), split='')


def safe_get(grid: grid, i: int, j: int) -> int:
    if 0 <= i < 10:
        if 0 <= j < 10:
            return grid[i][j]
    return -1


def step(grid: grid) -> int:
    for i, j in product(range(10), repeat=2):
        grid[i][j] += 1
    for i, j in product(range(10), repeat=2):
        if grid[i][j] == 10:
            flash(grid, i, j)
    return sum(1 for l in grid for x in l if x == 0)


def flash(grid: grid, i: int, j: int):
    grid[i][j] = 0
    for di, dj in product(range(-1, 2), repeat=2):
        ni, nj = i + di, j + dj
        val = safe_get(grid, ni, nj)
        if val == 9:
            flash(grid, ni, nj)
        elif 0 < val < 10:
            grid[ni][nj] += 1


def solution(grid: list[line_type]) -> solution_tuple:
    N = 1000
    flashes = 0
    for i in range(1, N):
        f = step(grid)
        flashes += f
        if i == 100:
            sol1 = flashes
        if f == 100:
            sol2 = i
            break
    return sol1, sol2

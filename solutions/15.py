from __future__ import annotations

from collections import defaultdict
from heapq import heappop, heappush
from itertools import product
from math import inf
from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import Iterable, TypeAlias

    from solutions.utils import solution_tuple

    point_type: TypeAlias = tuple[int, int]
    line_type: TypeAlias = list[int]

DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def neighbors(node: point_type) -> Iterable[point_type]:
    x, y = node
    for dx, dy in DELTAS:
        yield x + dx, y + dy


def h(node: point_type, end: point_type) -> int:
    """Return manhatten distance from `node` to `end`"""
    x, y = node
    dx, dy = end
    return dx - x + dy - y


def a_star(length: dict[point_type, int], start: point_type, end: point_type) -> int:
    g_score = defaultdict(lambda: inf)
    g_score[start] = 0
    open_set = []
    heappush(open_set, (0, start))

    while open_set:
        f, current = heappop(open_set)
        if current == end:
            return f
        for v in neighbors(current):
            alt = g_score[current] + length.get(v, inf)
            if alt < g_score[v]:
                g_score[v] = alt
                f_v = alt + h(v, end)
                heappush(open_set, (f_v, v))

    raise ValueError('Could not find end')


def line_parse(line: str) -> line_type:
    return ints(line.strip(), split='')


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    """
    Standard A* with manhatten distance as heuristic
    Compure hazard of point as described: point + #row + #col,
    wrap at 9 back to 1, i.e ((x-1) % 9) + 1
    """

    start = (0, 0)
    N = len(puzzle_input)

    lengths = {(i, j): puzzle_input[i][j] for i, j in product(range(N), repeat=2)}
    sol1 = a_star(lengths, start, (N - 1, N - 1))

    lengths = {
        (i, j): (lengths[(i % N, j % N)] + (i // N + j // N) - 1) % 9 + 1
        for i, j in product(range(5 * N), repeat=2)
    }
    sol2 = a_star(lengths, start, (5 * N - 1, 5 * N - 1))

    return sol1, sol2

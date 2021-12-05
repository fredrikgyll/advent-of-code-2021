from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import Iterator, TypeAlias, cast

    from solutions.utils import solution_tuple

    coord: TypeAlias = tuple[int, int]
    line_type: TypeAlias = tuple[coord, coord]


def line_parse(line: str) -> line_type:
    start, stop = line.strip().split(' -> ')
    start = tuple(ints(start, split=','))
    stop = tuple(ints(stop, split=','))
    if TYPE_CHECKING:
        start = cast(coord, start)
        stop = cast(coord, stop)
    return start, stop


def delta(start: coord, stop: coord) -> coord:
    """Return direction as a unit coorditate"""
    x = stop[0] - start[0]
    x = x // (abs(x) if x else 1)
    y = stop[1] - start[1]
    y = y // (abs(y) if y else 1)
    return x, y


def points(start: coord, stop: coord, delta: coord) -> Iterator[coord]:
    """Yield all points between state and stop"""
    nxt = start
    yield nxt
    dx, dy = delta
    while nxt != stop:
        nxt = nxt[0] + dx, nxt[1] + dy
        yield nxt


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    """
    Track visits to points on the grid.
    First only straight lines, then diagonals.
    """
    once = set()
    more_than_once = set()

    for start, stop in puzzle_input:
        d = delta(start, stop)
        if not (d[0] and d[1]):
            for p in points(start, stop, d):
                if p in once:
                    once.remove(p)
                    more_than_once.add(p)
                else:
                    once.add(p)
    sol1 = len(more_than_once)

    for start, stop in puzzle_input:
        d = delta(start, stop)
        if d[0] and d[1]:
            for p in points(start, stop, d):
                if p in once:
                    once.remove(p)
                    more_than_once.add(p)
                else:
                    once.add(p)
    sol2 = len(more_than_once)

    return sol1, sol2

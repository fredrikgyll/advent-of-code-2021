from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeAlias, cast

    from solutions.utils import solution_tuple

    map: TypeAlias = dict[str, set[str]]
    line_type: TypeAlias = tuple[str, str]


def paths(map: map, cave: str, visited: set[str], repeat: str | None = None) -> int:
    """Return number of paths from `cave` to `end`

    `visited`: small caves visited on current path
    `repeat`: small cave that has been visited twice on current path
    """
    if cave == 'end':
        return 1
    if cave.islower():
        visited = visited | {cave}
    num_paths = 0
    actions = map[cave]
    if next_destinations := actions - visited:
        num_paths += sum(paths(map, c, visited, repeat=repeat) for c in next_destinations)
    if not repeat and (reapeats := actions & visited):
        num_paths += sum(paths(map, r, visited, repeat=r) for r in reapeats)
    return num_paths


def line_parse(line: str) -> line_type:
    t = tuple(line.strip().split('-', maxsplit=1))
    if TYPE_CHECKING:
        t = cast(line_type, t)
    return t


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    """
    Create maping from caves to all valid destinations.
    do exhaustive search from `start` to `end` counting all paths
    """
    map = defaultdict(set)
    for x, y in puzzle_input:
        map[x].add(y)
        if x != 'start':
            map[y].add(x)

    sol1 = paths(map, 'start', set(), repeat='no')
    sol2 = paths(map, 'start', set())
    return sol1, sol2

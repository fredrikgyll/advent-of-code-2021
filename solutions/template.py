from __future__ import annotations

from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    line_type: TypeAlias = list[int]


def line_parse(line: str) -> line_type:
    return ints(line.strip())


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    sol1 = 1
    sol2 = 1
    return sol1, sol2

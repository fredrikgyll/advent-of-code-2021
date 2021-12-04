from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    line_type: TypeAlias = int

line_parse = int


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    sol1 = sum([x - y > 0 for x, y in zip(puzzle_input[1:], puzzle_input)])
    sol2 = sum([x - y > 0 for x, y in zip(puzzle_input[3:], puzzle_input)])
    return sol1, sol2

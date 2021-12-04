from __future__ import annotations

import re
from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    line_type: TypeAlias = str


def line_parse(line: str) -> line_type:
    return line.strip()


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    """
    With the chosen numbers, map the boards from value to round_when_picked.
    Bingo is the minimum of the maximum of each row+column.
    Finally, do a linear seach for the best/worst board.
    """
    numbers = ints(puzzle_input[0], split=',')
    num_map = {x: i for i, x in enumerate(numbers)}

    number_regex = re.compile(r'\d+')
    boards = [
        [ints(number_regex.findall(l)) for l in puzzle_input[i : i + 5]]
        for i in range(2, len(puzzle_input), 6)
    ]

    best_bingo = len(num_map)
    best_board = None

    worst_bingo = 0
    worst_board = None

    for board in boards:
        cols = list(zip(*board))
        bingo_on = min(max(num_map[x] for x in row) for row in board + cols)  # type: ignore
        if bingo_on < best_bingo:
            best_bingo = bingo_on
            best_board = board
        if bingo_on > worst_bingo:
            worst_bingo = bingo_on
            worst_board = board

    assert best_board
    assert worst_board

    def solve(board: list[list[int]], bingo: int) -> int:
        """Bingo is the round it occured so sum values where round_when_picked is higher"""
        flat_board = [x for l in board for x in l]
        unmarked = sum([x for x in flat_board if num_map[x] > bingo])
        bingo_number = numbers[bingo]
        return unmarked * bingo_number

    sol1 = solve(best_board, best_bingo)

    sol2 = solve(worst_board, worst_bingo)

    return sol1, sol2

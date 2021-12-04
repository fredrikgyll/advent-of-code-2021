from __future__ import annotations

from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    line_type: TypeAlias = list[int]


def line_parse(line: str) -> line_type:
    return ints(line.strip(), split='')


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    positions = list(zip(*puzzle_input))

    half = len(positions[0]) // 2
    gamma = [int(sum(pos) > half) for pos in positions]
    epsilon = [1 - x for x in gamma]

    gamma = ''.join(str(x) for x in gamma)
    epsilon = ''.join(str(x) for x in epsilon)

    sol1 = int(gamma, 2) * int(epsilon, 2)

    common_cand = puzzle_input
    lesser_cand = puzzle_input

    for i in range(len(positions)):
        if len(common_cand) != 1:
            common = int(sum(x[i] for x in common_cand) >= len(common_cand) / 2)
            common_cand = [x for x in common_cand if x[i] == common]
        if len(lesser_cand) != 1:
            common = int(sum(x[i] for x in lesser_cand) >= len(lesser_cand) / 2)
            lesser_cand = [x for x in lesser_cand if x[i] != common]

    o2 = ''.join(str(x) for x in common_cand[0])
    co2 = ''.join(str(x) for x in lesser_cand[0])

    sol2 = int(o2, 2) * int(co2, 2)

    return sol1, sol2

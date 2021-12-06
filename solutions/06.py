from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    line_type: TypeAlias = list[int]


def line_parse(line: str) -> line_type:
    return ints(line, split=',')


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    """
    Compute the growth of one fish, which grows on the first day.
    Treat the input as the ofset of that individuals growth from the
    one computed. Finally sum up the populations produced by each fish.

    `gaining` describes how many new fish are added n days from now.
    """

    current_population = 1
    population = [current_population]
    gaining = deque([0] * 8)
    gaining.appendleft(1)

    N_1 = 80
    N_2 = 256
    for _ in range(N_2):
        new = gaining.popleft()
        gaining.append(new)  # New fish will procreate at end of cycle
        gaining[6] += new  # Those who procreated, will repeat 6 days later
        current_population += new
        population.append(current_population)

    sol1 = sum(population[N_1 - x] for x in puzzle_input[0])
    sol2 = sum(population[N_2 - x] for x in puzzle_input[0])
    return sol1, sol2

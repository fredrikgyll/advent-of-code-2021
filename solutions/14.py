from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, Iterator

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    polymer_type: TypeAlias = dict[str, int]
    rules_type: TypeAlias = dict[str, tuple[str, str]]
    line_type: TypeAlias = str


def line_parse(line: str) -> line_type:
    return line.strip()


def pairs(template: str) -> Iterator[str]:
    for i in range(len(template) - 1):
        yield template[i : i + 2]


def count_bases(polymer: polymer_type, edge: str) -> int:
    counter: dict[str, float] = defaultdict(int)
    for el in edge:
        counter[el] += 0.5
    for pair, count in polymer.items():
        for base in pair:
            counter[base] += count / 2
    quantities = counter.values()
    return int(max(quantities) - min(quantities))


def polymerize(polymer: polymer_type, rules: rules_type, rounds: int) -> polymer_type:
    for _ in range(rounds):
        next_polymer = defaultdict(int)
        for pair, count in polymer.items():
            for next_pair in rules[pair]:
                next_polymer[next_pair] += count
        polymer = next_polymer
    return polymer


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    template = puzzle_input[0]
    edge = template[0] + template[-1]

    polymer: polymer_type = defaultdict(int)
    for pair in pairs(template):
        polymer[pair] += 1

    insertions = [l.split(' -> ', maxsplit=1) for l in puzzle_input[2:]]
    rules: rules_type = {x: (x[0] + y, y + x[1]) for x, y in insertions}

    polymer = polymerize(polymer, rules, 10)
    sol1 = count_bases(polymer, edge)

    polymer = polymerize(polymer, rules, 30)
    sol2 = count_bases(polymer, edge)

    return sol1, sol2

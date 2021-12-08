from __future__ import annotations

from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    cantitate_type: TypeAlias = list[set[str]]
    digits: TypeAlias = tuple[str, ...]
    line_type: TypeAlias = tuple[digits, digits]

MAPPING = {
    'cf': '1',
    'acf': '7',
    'bcdf': '4',
    'acdeg': '2',
    'acdfg': '3',
    'abdfg': '5',
    'abcefg': '0',
    'abdefg': '6',
    'abcdfg': '9',
    'abcdefg': '8',
}
FULL_SET = set('abcdefg')


def prune_singles(cand=list[set[str]]):
    """
    Apply constraint where digits that appear as the sole candidate
    in any position get removed from all other positions
    """
    for i, c in enumerate(cand):
        if len(c) == 1:
            for j in range(7):
                if i != j:
                    cand[j] -= c


def constrain_to(cand: cantitate_type, positions: list[int], digits: set[str]):
    """Apply constraint where `digits` can only appear in `positions`"""
    for i in range(7):
        if i in positions:
            cand[i] &= digits
        else:
            cand[i] -= digits


def remove_from(cand: cantitate_type, positions: list[int], digits: set[str]):
    """Apply constraint where `digits` cannot appear in `positions`"""
    for i in positions:
        cand[i] -= digits


def apply_digit_contraints(candidates: cantitate_type, digits: set[str]):
    n = len(digits)
    if n == 2:  #  Is a 1
        constrain_to(candidates, [2, 5], digits)
    if n == 3:  #  Is a 7
        constrain_to(candidates, [0, 2, 5], digits)
    if n == 4:  # Is a 4
        constrain_to(candidates, [1, 2, 3, 5], digits)
    if n == 6:  # Is a 0, 6, or 9
        missing = FULL_SET - digits
        remove_from(candidates, [0, 1, 5, 6], missing)


def translate(digit: str, key: dict[str, str]) -> str:
    translated = ''.join(sorted([key[c] for c in digit]))
    return MAPPING[translated]


def line_parse(line: str) -> line_type:
    digits, output = line.strip().split(' | ')
    return tuple(digits.split(' ')), tuple(output.split(' '))


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    unique_digits = [2, 3, 4, 7]
    outputs = [len(x) for _, o in puzzle_input for x in o]
    sol1 = sum(1 for x in outputs if x in unique_digits)

    corrected: list[int] = []
    for signals, output in puzzle_input:
        candidates = [set('abcdefg') for _ in range(7)]
        for signal in signals:
            apply_digit_contraints(candidates, set(signal))
        prune_singles(candidates)

        assert all(len(c) == 1 for c in candidates)
        key = {c.pop(): alph for c, alph in zip(candidates, 'abcdefg')}
        out = int(''.join(translate(d, key) for d in output))

        corrected.append(out)

    sol2 = sum(corrected)
    return sol1, sol2

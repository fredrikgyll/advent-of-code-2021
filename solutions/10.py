from __future__ import annotations

from functools import reduce
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    line_type: TypeAlias = str


def is_open(open_bracket: str) -> bool:
    return open_bracket in '{[(<'


def matches(closed_bracket: str, open_bracket: str) -> bool:
    return {'>': '<', '}': '{', ']': '[', ')': '('}[closed_bracket] == open_bracket


def score_error(closed_bracket: str) -> int:
    return {'>': 25137, '}': 1197, ']': 57, ')': 3}[closed_bracket]


def score_completion(open_bracket: str) -> int:
    return {'<': 4, '{': 3, '[': 2, '(': 1}[open_bracket]


def completion_op(a: int, b: int) -> int:
    return a * 5 + b


def line_parse(line: str) -> line_type:
    return line.strip()


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    """
    Use stack to track open brackets and cker for errors.
    Brackets left on stack are incomplete in revered order
    """
    error_score = 0
    incomplete = []

    for line in puzzle_input:
        stack = []
        error = 0
        for bracket in line:
            if is_open(bracket):
                stack.append(bracket)
            else:
                match = stack.pop()
                if not matches(bracket, match):
                    error = score_error(bracket)
                    break
        if error:
            error_score += error
        else:
            incomplete.append(stack[::-1])

    sol1 = error_score

    completions = [[score_completion(c) for c in line] for line in incomplete]
    completion_scores = [reduce(completion_op, l, 0) for l in completions]
    middle = len(completion_scores) // 2

    sol2 = sorted(completion_scores)[middle]

    return sol1, sol2

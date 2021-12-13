from __future__ import annotations

from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import TypeAlias, cast

    from solutions.utils import solution_tuple

    points_type: TypeAlias = set[tuple[int, int]]
    line_type: TypeAlias = str


def line_parse(line: str) -> line_type:
    return line.strip()


def command_parse(line: str) -> tuple[int, int]:
    fold, at = line.split('=')
    idx = 0 if fold[-1] == 'x' else 1
    return idx, int(at)


def fold(points: points_type, command: tuple[int, int]) -> points_type:
    folded = set()
    idx, fold = command
    for point in points:
        p = point[idx]
        new_point = list(point)
        if p > fold:
            new_point[idx] = 2 * fold - p
        folded.add(tuple(new_point))
    return folded


def format_points(points: points_type):
    fmt = ['\n']
    transpose = list(zip(*points))
    X, Y = max(transpose[0]), max(transpose[1])
    for y in range(Y + 1):
        line = []
        for x in range(X + 1):
            chr = '█' if (x, y) in points else ' '
            line.append(chr)
        fmt.append(''.join(line))
    return '\n'.join(fmt)


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    points = {tuple(ints(l.split(','))) for l in puzzle_input if l and l[0].isdigit()}
    if TYPE_CHECKING:
        points = cast(points_type, points)
    commands = [command_parse(l) for l in puzzle_input if l.startswith('f')]

    points = fold(points, commands[0])

    sol1 = len(points)

    for command in commands[1:]:
        points = fold(points, command)
    sol2 = format_points(points)

    return sol1, sol2

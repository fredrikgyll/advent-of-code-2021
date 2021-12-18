from __future__ import annotations

import re
from math import sqrt
from typing import TYPE_CHECKING

from solutions.utils import ints

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    line_type: TypeAlias = list[tuple[int, int]]

reg = re.compile(r'.+x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)')


def line_parse(line: str) -> line_type:
    m = reg.match(line.strip())
    assert m
    x1, x2, y1, y2 = ints(list(m.groups()))
    return [(x1, x2), (y1, y2)]


def nat_sum(n: int):
    return (n * (n - 1)) // 2


def y_step(init_y: int, terminal_y: int) -> float:
    """
    Return floating point step when projectile is at `terminal_y`

    Solves the formula for aritmetic sum for `n` and returns
    the valid root fo the quadratic
    """
    a = 2 * init_y + 1
    b = 2 * terminal_y
    det = a ** 2 - 4 * b

    n1 = 0.5 * (a - sqrt(det))
    n2 = 0.5 * (a + sqrt(det))

    return max(n1, n2)


def x_dist(init_vel: int, step: int) -> int:
    """Return distance traveled in x positive direction"""
    term = min(step, init_vel)
    a_n = init_vel - (term - 1)
    return (term * (init_vel + a_n)) // 2


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    """
    For Part 1 assume peak when particle hits lower bound of target
    and find distance at y_velocity = 0

    For Part 2 first for all possible y velocities find the step number(s)
    where the particle is at a valid y-position, i.e. when `y_step` is an
    integer. Then for all these step values, find which x_velocities will deliver
    the particle to the target at that step.
    """
    X, Y = puzzle_input[0]
    at_lower_bound = abs(Y[0])
    sol1 = nat_sum(at_lower_bound)

    max_x_vel = X[1] + 1
    min_y_vel = Y[0]
    max_y_vel = abs(Y[0])

    y_steps = {}
    for y in range(min_y_vel, max_y_vel + 1):
        steps = [y_step(y, i) for i in range(Y[0], Y[1] + 1)]
        y_steps[y] = {int(i) for i in steps if i.is_integer()}

    x_vels = {}
    for s in range(1, 2 + max_y_vel * 2):
        x_vels[s] = [i for i in range(max_x_vel + 1) if X[0] <= x_dist(i, s) <= X[1]]

    vels = set()
    for y_vel, steps in y_steps.items():
        for step in steps:
            vels |= {(x, y_vel) for x in x_vels[step]}

    sol2 = len(vels)
    return sol1, sol2

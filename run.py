#!/usr/bin/env python3

from datetime import datetime
from importlib import import_module

import click

day = datetime.now().day

from solutions.utils import get_input


@click.command()
@click.option('--day', default=day, type=int, help='Which day to run')
@click.option('--debug', is_flag=True, help='Run with test input')
def main(day: int, debug: bool):
    click.secho(f'*** AoC Day {day} ***\n', fg='green')
    solution_module = import_module(f'solutions.{day:02d}')
    puzzle_input = get_input(solution_module.line_parse, day, debug)
    part1, part2 = solution_module.solution(puzzle_input)

    if debug:
        click.secho('Using the test input!', fg='red')
    if part1:
        click.echo('Part 1: ', nl=False)
        click.secho(part1, fg='yellow')
    if part2:
        click.echo('Part 2: ', nl=False)
        click.secho(part2, fg='yellow')


if __name__ == '__main__':
    main()

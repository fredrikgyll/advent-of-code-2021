#!/usr/bin/env python3

import os
from datetime import datetime
from pathlib import Path

import click
import requests
from dotenv import load_dotenv

day = datetime.now().day


@click.command()
@click.option('--day', default=day, type=int, help='Which day to get')
def get(day):
    root = f'https://adventofcode.com/2021/day/{day}'
    session = os.getenv('AOC_SESSION')
    resp = requests.get(root + '/input', cookies={'session': session})
    resp.raise_for_status()

    out_file = Path(f'./input/{day:02d}.txt')
    out_file.write_text(resp.text)

    test_file = Path(f'./input/{day:02d}-test.txt')
    if not test_file.is_file():
        test_file.touch()

    solution_file = Path(f'./solutions/{day:02d}.py')
    if not solution_file.is_file():
        solution_file.write_bytes(Path(f'./solutions/template.py').read_bytes())

    click.echo(f'Fetching day {day} complete. Link to challenge:\n\t{root}')


if __name__ == '__main__':
    load_dotenv()
    get()

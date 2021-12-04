from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import TypeAlias, TypeVar

    T = TypeVar('T')

    solution_type: TypeAlias = int | str
    solution_tuple: TypeAlias = tuple[solution_type, solution_type]

__all__ = ('get_input', 'ints', 'solution_tuple')


def get_input(line_parser: Callable[[str], T], day: int, debug: bool) -> list[T]:
    file_name = f'{day:02d}'
    if debug:
        file_name += '-test'
    infile = Path(f'./input/{file_name}.txt')
    assert infile.is_file(), 'No infile found'
    with infile.open() as f:
        lines = [line_parser(line) for line in f.readlines()]
    return lines


def ints(l: list[str] | str, split: str = ' ', base: int = 10) -> list[int]:
    lst = None
    if isinstance(l, str):
        if split:
            lst = l.split(split)
    return [int(x, base) for x in lst or l]

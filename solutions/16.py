from __future__ import annotations

from operator import mul
from functools import reduce
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeAlias

    from solutions.utils import solution_tuple

    packet_type: TypeAlias = dict[str, int | list]
    line_type: TypeAlias = str


def line_parse(line: str) -> line_type:
    return line.strip()


def cut(bytes: str, n: int) -> tuple[str, str]:
    return bytes[:n], bytes[n:]


def cut_i(bytes: str, n: int) -> tuple[int, str]:
    return int(bytes[:n], 2), bytes[n:]


def parse_packet(bytes: str) -> tuple[int, int, str]:
    ver, bytes = cut_i(bytes, 3)
    typ, bytes = cut_i(bytes, 3)
    content = 0
    if typ == 4:
        leading, bytes = cut_i(bytes, 1)
        num, bytes = cut(bytes, 4)
        while leading == 1:
            leading, bytes = cut_i(bytes, 1)
            partial, bytes = cut(bytes, 4)
            num += partial
        content = int(num, 2)
    else:
        l_type, bytes = cut_i(bytes, 1)
        sub_packets = []
        if l_type == 1:
            num, bytes = cut_i(bytes, 11)
            for _ in range(num):
                sub_ver, sub_content, bytes = parse_packet(bytes)
                sub_packets.append(sub_content)
                ver += sub_ver
        else:
            n_bits, bytes = cut_i(bytes, 15)
            sub_bits, bytes = cut(bytes, n_bits)
            while sub_bits:
                sub_ver, sub_content, sub_bits = parse_packet(sub_bits)
                sub_packets.append(sub_content)
                ver += sub_ver

        if typ == 0:
            content = sum(sub_packets)
        elif typ == 1:
            content = reduce(mul, sub_packets, 1)
        elif typ == 2:
            content = min(sub_packets)
        elif typ == 3:
            content = max(sub_packets)
        else:
            first, second = sub_packets
            if typ == 5:
                content = 1 if first > second else 0
            elif typ == 6:
                content = 1 if first < second else 0
            elif typ == 7:
                content = 1 if first == second else 0
    return ver, content, bytes


def solution(puzzle_input: list[line_type]) -> solution_tuple:
    hex = puzzle_input[0]
    n_bits = len(hex) * 4
    b = bin(int(puzzle_input[0], 16))[2:].zfill(n_bits)

    sol1, sol2, _ = parse_packet(b)

    return sol1, sol2

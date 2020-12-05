#!/usr/bin/env python

import math


def parse_input_file(filename: str):
    parsed_lines = []
    with open(filename) as input_file:
        parsed_lines = [
                (li[:7], li[7:]) for li in input_file.read().splitlines()
        ]
    return parsed_lines


def find_mid(low, high):
    return (high + low) / 2


def find_spot(
    code,
    low,
    high,
    low_char,
    high_char,
):
    for char in code:
        mid = find_mid(low, high)
        if char == low_char:
            high = int(math.floor(mid))
        else:
            low = int(math.ceil(mid))
    assert(high == low)
    return high


def gen_seat_id(row, column):
    return (8 * row) + column


def find_my_seat(seat_ids):
    for x in range(min(seat_ids), max(seat_ids)):
        if x not in seat_ids:
            return x


if __name__ == "__main__":
    data = parse_input_file('input.txt')
    seat_ids = []

    for row_code, col_code in data:
        row = find_spot(
            row_code, 0, 127, 'F', 'B'
        )
        col = find_spot(
            col_code, 0, 7, 'L', 'R'
        )
        seat_id = gen_seat_id(row, col)
        seat_ids.append(seat_id)

    part_1_result = max(seat_ids)
    print(f"Part 1: {part_1_result}")

    part_2_result = find_my_seat(seat_ids)
    print(f"Part 2: {part_2_result}")

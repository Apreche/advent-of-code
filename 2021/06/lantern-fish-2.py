#!/usr/bin/env python

import functools
import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    parsed_input = []
    with open(full_file_path) as input_file:
        raw_line = input_file.readline()
        parsed_input = [int(x) for x in raw_line.split(',')]
    return parsed_input


@functools.cache
def process_one_fish(current_value, remaining_days):
    fish_total = 1
    days_until_birth = current_value + 1
    if days_until_birth <= remaining_days:
        fish_total += process_one_fish(
            6, remaining_days - days_until_birth
        ) - 1
        fish_total += process_one_fish(
            6, remaining_days - days_until_birth - 2
        )
    return fish_total


def process_all_fish(today, num_days=80):
    return sum([process_one_fish(fish, num_days) for fish in today])


def main():
    parsed_input = parse_input_file("input.txt")

    part_1_result = process_all_fish(parsed_input, num_days=80)
    print(f"Part 1: {part_1_result}")

    part_2_result = process_all_fish(parsed_input, num_days=256)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

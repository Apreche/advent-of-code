#!/usr/bin/env python

import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    parsed_input = []
    with open(full_file_path) as input_file:
        raw_line = input_file.readline()
        parsed_input = [int(x) for x in raw_line.split(',')]
    return parsed_input


def get_next_day(today):
    tomorrow = []
    for fish in today:
        if fish == 0:
            tomorrow += [6, 8]
        else:
            tomorrow.append(fish - 1)
    return tomorrow


def process_fish(today, num_days=80):
    for day in range(num_days):
        today = get_next_day(today)
    return today


def main():
    # parsed_input = parse_input_file("test_input.txt")
    parsed_input = parse_input_file("input.txt")

    processed_fish = process_fish(parsed_input)
    part_1_result = len(processed_fish)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

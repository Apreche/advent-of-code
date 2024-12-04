#!/usr/bin/env python

import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            pair = line.split(',')
            parsed_pair = []
            for assignment in pair:
                low, high = assignment.split("-")
                parsed_pair.append(
                    (int(low), int(high))
                )
            parsed_input.append(tuple(parsed_pair))

    return parsed_input


def is_pair_fully_contained(pair):
    first, second = pair
    first_low, first_high = first
    second_low, second_high = second
    first_contains = (
        (first_low <= second_low) and (first_high >= second_high)
    )
    second_contains = (
        (second_low <= first_low) and (second_high >= first_high)
    )
    return first_contains or second_contains


def is_pair_overlapping(pair):
    first, second = pair
    first_low, first_high = first
    second_low, second_high = second
    first_assignment = set(range(first_low, first_high+1))
    second_assignment = set(range(second_low, second_high+1))
    return bool(first_assignment.intersection(second_assignment))


def count_fully_contains(pairs):
    count = 0
    for pair in pairs:
        if is_pair_fully_contained(pair):
            count += 1
    return count


def count_overlapping(pairs):
    count = 0
    for pair in pairs:
        if is_pair_overlapping(pair):
            count += 1
    return count


def main():
    parsed_input = parse_input_file("input.txt")

    part_1_result = count_fully_contains(parsed_input)
    print(f"Part 1: {part_1_result}")

    part_2_result = count_overlapping(parsed_input)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python

import string
import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input


def get_priority(letter):
    return string.ascii_letters.index(letter) + 1


def find_common_item(compartments=()):
    first_set, *other_sets = (set(compartment) for compartment in compartments)
    common_set = first_set.intersection(*other_sets)
    assert len(common_set) == 1
    return common_set.pop()


def halve_sacks(sacks=[]):
    split_sacks = []
    for sack in sacks:
        split_index = len(sack) // 2
        split_sacks.append(
            (
                sack[:split_index],
                sack[split_index:],
            )
        )
    return split_sacks


def group_sacks_by_n(sacks, n):
    return [sacks[i:i+n] for i in range(0, len(sacks), n)]


def calculate_part_1(parsed_input):
    divided_sacks = halve_sacks(parsed_input)
    score = sum(
        [
            get_priority(
                find_common_item(sack)
            )
            for sack in divided_sacks
        ]
    )
    return score


def calculate_part_2(parsed_input):
    grouped_sacks = group_sacks_by_n(parsed_input, 3)
    score = sum(
        [
            get_priority(
                find_common_item(sack)
            )
            for sack in grouped_sacks
        ]
    )
    return score


def main():
    parsed_input = parse_input_file("input.txt")

    part_1_result = calculate_part_1(parsed_input)
    print(f"Part 1: {part_1_result}")

    part_2_result = calculate_part_2(parsed_input)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

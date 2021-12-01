#!/usr/bin/env python

import os

def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:

        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(int(line))
    return parsed_input

def get_num_depth_increases(depths):
    num_increases = 0
    current_val = None
    for depth in depths:
        if current_val is not None:
            if depth > current_val:
                num_increases += 1
        current_val = depth
    return num_increases


def main():
    parsed_input = parse_input_file("input.txt")

    part_1_result = get_num_depth_increases(parsed_input)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

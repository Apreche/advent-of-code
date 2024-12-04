#!/usr/bin/env python

import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        return input_file.read().rstrip()


def find_start_marker(signal, window=4):
    for index in range(0, len(signal)-window):
        sample = set(signal[index:index+window])
        if len(sample) == window:
            return index + window


def main():
    parsed_input = parse_input_file("input.txt")

    part_1_result = find_start_marker(parsed_input)
    print(f"Part 1: {part_1_result}")

    part_2_result = find_start_marker(parsed_input, window=14)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

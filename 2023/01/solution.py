#!/usr/bin/env python
from typing import List

import os
import re

def parse_input_file(filename: str) -> List[str]:
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input

def get_calibration_value(text: str) -> int:
    digits_only = re.sub(r"[^1-9]", "", text)
    first_digit = digits_only[0]
    last_digit = digits_only[-1]
    return int(f"{first_digit}{last_digit}")

def sum_calibration_values(text: List[str]) -> int:
    calibration_values = []
    for line in text:
        calibration_values.append(get_calibration_value(line))
    return sum(calibration_values)

digit_map = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
def get_advanced_calibration_value(text: str):
    left_value = None
    left_index = None
    right_value = None
    right_index = None
    for search, digit in digit_map.items():
        first_index = text.find(search)
        if first_index >= 0:
            if (left_index is None) or (first_index < left_index):
                left_index = first_index
                left_value = digit
        last_index = text.rfind(search)
        if last_index >= 0:
            if(right_index is None) or (last_index > right_index):
                right_index = last_index
                right_value = digit
    return int(f"{left_value}{right_value}")

def sum_advanced_calibration_values(text: List[str]) -> int:
    calibration_values = []
    for line in text:
        calibration_values.append(get_advanced_calibration_value(line))
    return sum(calibration_values)

def main() -> None:
    parsed_input = parse_input_file("input.txt")

    part_1_result = sum_calibration_values(parsed_input)
    print(f"Part 1: {part_1_result}")

    part_2_result = sum_advanced_calibration_values(parsed_input)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

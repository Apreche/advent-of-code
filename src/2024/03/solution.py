#!/usr/bin/env python

import os
import re
import typing


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input


def mul_pairs_from_line(line: str) -> typing.List[typing.Tuple[int, int]]:
    pattern = r"mul\((\d{1,3})\,(\d{1,3})\)"
    string_pairs = [x.groups() for x in re.finditer(pattern, line)]
    return [(int(x), int(y)) for x, y in string_pairs]


def mul_all_lines(lines: typing.List[str]) -> int:
    pairs = []
    for line in lines:
        pairs += mul_pairs_from_line(line)
    return sum([x * y for x, y in pairs])


def remove_disabled_sections(lines: typing.List[str]) -> str:
    combined_lines = "".join(lines)
    pattern = r"(don\'t\(\)).*?((do\(\))|$)"
    return [re.sub(pattern, "", combined_lines)]


def main():
    parsed_input = parse_input_file("input.txt")

    part_1_result = mul_all_lines(parsed_input)
    print(f"Part 1: {part_1_result}")

    part_2_result = mul_all_lines(remove_disabled_sections(parsed_input))
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

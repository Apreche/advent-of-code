#!/usr/bin/env python

import os
import operator


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input


operator_lookup = {
    "+": operator.add,
    "-": operator.sub,
}


def operate(operations=[], start_val=0):
    result = start_val
    for operation in operations:
        operator_str, *value_str = operation
        value = int("".join(value_str))
        result = operator_lookup[operator_str](result, value)
    return result


def main():
    parsed_input = parse_input_file("test_input.txt")

    part_1_result = operate(parsed_input, 0)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

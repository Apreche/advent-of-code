#!/usr/bin/env python

import copy
import re
import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        raw_stacks = []
        raw_instructions = []
        below_empty_line = False
        for line in input_file.read().splitlines():
            if not below_empty_line:
                if not line:
                    below_empty_line = True
                    continue
                raw_stacks.append(line)
            else:
                raw_instructions.append(line)
    return raw_stacks, raw_instructions


def parse_stacks(raw_crates):
    stack_numbers = [int(n) for n in raw_crates.pop().split()]
    num_stacks = max(stack_numbers)
    stacks = [[] for _ in range(num_stacks)]
    raw_crates.reverse()
    for row in raw_crates:
        parsed_row = [row[i] for i in range(1, len(row), 4)]
        for index, crate in enumerate(parsed_row):
            if crate != " ":
                stacks[index].append(crate)
    return stacks


def parse_instructions(raw_instructions):
    pattern = re.compile(r"^move (\d+) from (\d+) to (\d+)$")
    parsed_instructions = []
    for raw_instruction in raw_instructions:
        match = pattern.match(raw_instruction)
        assert match is not None
        parsed_instruction = tuple(int(num) for num in match.groups())
        parsed_instructions.append(parsed_instruction)

    return parsed_instructions


def execute_instructions_9000(stacks, instructions):
    result_stacks = copy.deepcopy(stacks)
    for instruction in instructions:
        quantity, from_stack, to_stack = instruction
        for _ in range(quantity):
            result_stacks[to_stack - 1].append(
                result_stacks[from_stack - 1].pop()

            )

    return result_stacks


def execute_instructions_9001(stacks, instructions):
    result_stacks = copy.deepcopy(stacks)
    for instruction in instructions:
        quantity, from_stack, to_stack = instruction
        result_stacks[to_stack-1] += result_stacks[from_stack-1][-quantity:]
        result_stacks[from_stack-1] = result_stacks[from_stack-1][:-quantity]

    return result_stacks


def read_top_crates(stacks):
    result = []
    for stack in stacks:
        if stack:
            result.append(stack[-1])
    return result


def main():
    raw_starting_stacks, raw_instructions = parse_input_file("input.txt")
    parsed_stacks = parse_stacks(raw_starting_stacks)
    parsed_instructions = parse_instructions(raw_instructions)
    processed_stacks = execute_instructions_9000(
        parsed_stacks, parsed_instructions)
    part_1_result = read_top_crates(processed_stacks)
    print(f"Part 1: {part_1_result}")

    raw_starting_stacks, _ = parse_input_file("input.txt")
    parsed_stacks = parse_stacks(raw_starting_stacks)
    processed_stacks = execute_instructions_9001(
        parsed_stacks, parsed_instructions)
    part_2_result = read_top_crates(processed_stacks)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

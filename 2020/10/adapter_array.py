#!/usr/bin/env python

def parse_input_file(filename: str):

    with open(filename) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(int(line))
    return sorted(parsed_input)


def count_jolt_jumps(adapters):
    joltage = 0
    jumps = {1: 0, 2: 0, 3: 1}
    for adapter in adapters:
        jump_size = adapter - joltage
        jumps[jump_size] += 1
        joltage = adapter
    return jumps


def main():
    parsed_input = parse_input_file("input.txt")
    jumps = count_jolt_jumps(parsed_input)
    part_1_result = jumps[1] * jumps[3]

    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

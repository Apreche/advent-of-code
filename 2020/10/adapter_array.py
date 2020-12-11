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


def jolt_jump_sequence(adapters):
    adapters.insert(0, 0)
    current_joltage = 0
    jumps = []
    for adapter in adapters:
        jumps.append(adapter - current_joltage)
        current_joltage = adapter
    return jumps


def ones_in_a_row(sequence):
    sequence.append(3)
    ones_in_a_row = []
    current_count = 0
    for x in sequence:
        if x == 1:
            current_count += 1
        else:
            ones_in_a_row.append(current_count)
            current_count = 0
    return ones_in_a_row


def count_possibilities(chains):
    lookup = [1, 1, 2, 4, 7]
    possibilities = 1
    for chain in chains:
        times = lookup[chain]
        possibilities *= times
    return possibilities


def main():
    parsed_input = parse_input_file("input.txt")
    jumps = count_jolt_jumps(parsed_input)
    part_1_result = jumps[1] * jumps[3]

    print(f"Part 1: {part_1_result}")

    sequence = jolt_jump_sequence(parsed_input)
    one_chains = ones_in_a_row(sequence)
    part_2_result = count_possibilities(one_chains)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

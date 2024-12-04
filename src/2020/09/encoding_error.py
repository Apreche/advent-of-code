#!/usr/bin/env python

import itertools


def parse_input_file(filename: str):

    with open(filename) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(int(line))
    return parsed_input


def validate_number(preamble, number):
    combos = itertools.combinations(preamble, 2)
    sums = [sum(x) for x in combos]
    if number in sums:
        return True
    return False


def find_first_invalid(numbers, preamble_length):
    offset = 0
    while offset + preamble_length <= len(numbers):
        preamble = numbers[offset:offset+preamble_length]
        number = numbers[offset+preamble_length]
        if not validate_number(preamble, number):
            return number
        offset += 1
    return False


def find_weak_range(numbers, target, minimum_slit=2):
    offset = 0
    while offset <= len(numbers) - minimum_slit:
        slit_size = minimum_slit
        while offset + slit_size <= len(numbers):
            current_range = numbers[offset:offset+slit_size]
            found_sum = sum(current_range)
            if found_sum == target:
                return current_range
            if found_sum > target:
                break
            slit_size += 1
        offset += 1
    return False


def find_weakness(number_range):
    return min(number_range) + max(number_range)


def main():
    numbers = parse_input_file('input.txt')
    part_1_result = find_first_invalid(numbers, 25)
    print(f"Part 1: {part_1_result}")

    weak_range = find_weak_range(numbers, part_1_result)
    part_2_result = find_weakness(weak_range)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

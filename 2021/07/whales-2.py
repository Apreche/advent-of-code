#!/usr/bin/env python

import functools
import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = [int(x) for x in input_file.readline().split(',')]
    return parsed_input


@functools.cache
def get_triangular_number(number):
    return (number * (number + 1)) // 2


def calculate_fuel(crabs):
    results = {}
    for meetup_point in range(0, max(crabs)):
        fuel = sum([abs(crab - meetup_point) for crab in crabs])
        results[meetup_point] = fuel
    return results


def calculate_triangular_fuel(crabs):
    results = {}
    for meetup_point in range(0, max(crabs)):
        fuel = sum(
            [get_triangular_number(abs(crab - meetup_point)) for crab in crabs]
        )
        results[meetup_point] = fuel
    return results


def main():
    parsed_input = parse_input_file("input.txt")

    fuel_usage = calculate_fuel(parsed_input)
    part_1_result = min(fuel_usage.values())
    print(f"Part 1: {part_1_result}")

    triangular_fuel_usage = calculate_triangular_fuel(parsed_input)
    part_2_result = min(triangular_fuel_usage.values())
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

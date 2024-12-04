#!/usr/bin/env python

import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(
                [int(x) for x in line]
            )
    return parsed_input


def flip(x):
    if x == 1:
        return 0
    return 1


def calculate_gamma_epsilon(data):
    num_numbers = len(data)
    data.reverse()
    rotated_data = zip(*data)
    epsilon_list = []
    for column in rotated_data:
        if sum(column) / num_numbers > 0.5:
            epsilon_list.append(1)
        else:
            epsilon_list.append(0)
    gamma_list = [flip(x) for x in epsilon_list]
    epsilon = int(''.join([str(x) for x in epsilon_list]), 2)
    gamma = int(''.join([str(x) for x in gamma_list]), 2)
    return epsilon, gamma


def main():
    parsed_input = parse_input_file("input.txt")
    epsilon, gamma = calculate_gamma_epsilon(parsed_input)
    power_consumption = epsilon * gamma

    part_1_result = power_consumption
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

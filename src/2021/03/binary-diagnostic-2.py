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


def rotate_and_sum(data):
    num_numbers = len(data)
    results = []
    data.reverse()
    rotated_data = zip(*data)
    for column in rotated_data:
        if sum(column) / num_numbers >= 0.5:
            results.append(1)
        else:
            results.append(0)
    return results


def bin_str_to_int(value):
    return int(''.join([str(x) for x in value]), 2)


def calculate_gamma_epsilon(data):
    epsilon_list = rotate_and_sum(data)
    gamma_list = [flip(x) for x in epsilon_list]
    epsilon = bin_str_to_int(epsilon_list)
    gamma = bin_str_to_int(gamma_list)
    return epsilon, gamma


def calculate_oxygen(data, flip=False):
    for i in range(len(data[0])):
        winners = rotate_and_sum(data)
        if flip:
            data = [x for x in data if x[i] != winners[i]]
        else:
            data = [x for x in data if x[i] == winners[i]]
        if len(data) == 1:
            break
    return bin_str_to_int(data[0])


def calculate_scrubber(data):
    return calculate_oxygen(data, flip=True)


def main():
    parsed_input = parse_input_file("input.txt")
    epsilon, gamma = calculate_gamma_epsilon(parsed_input)
    power_consumption = epsilon * gamma

    part_1_result = power_consumption
    print(f"Part 1: {part_1_result}")

    oxygen = calculate_oxygen(parsed_input)
    scrubber = calculate_scrubber(parsed_input)
    life_support_rating = oxygen * scrubber

    part_2_result = life_support_rating
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python

import os


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input


def calcualte_elf_calories(inventory_list):
    elves = []
    current_elf = 0
    for item in inventory_list:
        if item:
            current_elf += int(item)
        else:
            elves.append(current_elf)
            current_elf = 0
    if current_elf != 0:
        elves.append(current_elf)
    return elves


def elf_with_most(inventory_list):
    elf_list = calcualte_elf_calories(inventory_list)
    return max(elf_list)


def top_three_total(inventory_list):
    elf_list = calcualte_elf_calories(inventory_list)
    sorted_elf_list = sorted(elf_list, reverse=True)
    top_three = sorted_elf_list[:3]
    return sum(top_three)


def main():
    parsed_input = parse_input_file("input.txt")

    part_1_result = elf_with_most(parsed_input)
    print(f"Part 1: {part_1_result}")

    part_2_result = top_three_total(parsed_input)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

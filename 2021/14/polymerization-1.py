#!/usr/bin/env python

import os


def one_step(template, rules):
    polymer = []
    for index in range(len(template) - 1):
        pair = template[index:index+2]
        insert = rules[pair]
        polymer.append(template[index])
        polymer.append(insert)
    polymer.append(template[-1])
    return "".join(polymer)


def polymerize(template, rules, steps=10):
    polymer = template
    for _ in range(steps):
        polymer = one_step(polymer, rules)
    return polymer


def polymer_count(polymer):
    most_common = max(polymer, key=polymer.count)
    least_common = min(polymer, key=polymer.count)
    return polymer.count(most_common) - polymer.count(least_common)


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        template = input_file.readline().strip()
        input_file.readline()  # skip a line
        rules = {}
        for line in input_file.read().splitlines():
            pair, insertion = line.strip().split(' -> ')
            rules[pair] = insertion
    return template, rules


def main():
    template, rules = parse_input_file("input.txt")

    part_1_polymer = polymerize(template, rules, steps=10)
    part_1_result = polymer_count(part_1_polymer)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

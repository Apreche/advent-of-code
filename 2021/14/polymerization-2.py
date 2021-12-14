#!/usr/bin/env python

import os


def polymerize(template, rules, steps=10):
    pairs = {}
    final_char = template[-1]

    for index in range(len(template) - 1):
        pair = template[index:index+2]
        pairs.setdefault(pair, 0)
        pairs[pair] += 1

    for _ in range(steps):
        new_pairs = {}
        for pair, count in pairs.items():
            new_char = rules[pair]
            new_pairs.setdefault(pair[0] + new_char, 0)
            new_pairs.setdefault(new_char + pair[1], 0)
            new_pairs[pair[0] + new_char] += count
            new_pairs[new_char + pair[1]] += count
        pairs = new_pairs
    return pairs, final_char


def polymer_count(pairs, final_char):
    counts = {final_char: 1}
    for key, count in pairs.items():
        char = key[0]
        counts.setdefault(char, 0)
        counts[char] += count
    return max(counts.values()) - min(counts.values())


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

    part_1_pairs, part_1_final = polymerize(template, rules, steps=10)
    part_1_result = polymer_count(part_1_pairs, part_1_final)
    print(f"Part 1: {part_1_result}")

    part_2_pairs, part_2_final = polymerize(template, rules, steps=40)
    part_2_result = polymer_count(part_2_pairs, part_2_final)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

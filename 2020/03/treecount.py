#!/usr/bin/env python

import math

TREE = '#'


def parse_input_file(filename: str):
    parsed_lines = []
    with open(filename) as input_file:
        parsed_lines = [li for li in input_file.read().splitlines()]
    return parsed_lines


def count_trees(data, horizontal, vertical):
    width = len(data[0])
    height = len(data)
    x = 0
    y = 0
    tree_count = 0

    while y + vertical < height:
        x += horizontal
        y += vertical
        if data[y][x % width] == TREE:
            tree_count += 1
    return tree_count


def count_slopes(data, slopes=[]):
    tree_counts = []
    for horizontal, vertical in slopes:
        tree_counts.append(
            count_trees(
                data,
                horizontal,
                vertical
            )
        )
    return tree_counts


if __name__ == "__main__":
    data = parse_input_file('input.txt')

    part_1_result = count_trees(data, 3, 1)
    print(f"Part 1: {part_1_result}")

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    tree_counts = count_slopes(data, slopes)
    part_2_result = math.prod(tree_counts)

    print(f"Part 2: {part_2_result}")

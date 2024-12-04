#!/usr/bin/env python

import typing
import os
import collections


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input

def input_to_lists(input: typing.List[str]) -> typing.Tuple[typing.List[int], typing.List[int]]:
    left_list = []
    right_list = []
    for row in input:
        left_value, right_value = row.split("   ")
        left_list.append(int(left_value))
        right_list.append(int(right_value))
    return left_list, right_list

def lists_to_sorted_tuples(left_list: typing.List[int], right_list: typing.List[int]) -> typing.List[typing.Tuple[int, int]]:
    assert(len(left_list) == len(right_list))
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    result = []
    for index in range(len(sorted_left)):
        result.append((sorted_left[index], sorted_right[index]))
    return result

def distance(x: int, y:int) -> int:
    return abs(x-y)

def distance_list(sorted_tuples: typing.List[typing.Tuple[int, int]]) -> typing.List[int]:
    return [distance(x, y) for x, y in sorted_tuples]

def total_list_distance(left_list: typing.List[int], right_list: typing.List[int]) -> int:
    sorted_tuples = lists_to_sorted_tuples(left_list, right_list)
    return sum(distance_list(sorted_tuples))

def similarity_score(left_list: typing.List[int], right_list: typing.List[int]) -> int:
    similarity_score = 0
    counter = collections.Counter(right_list)
    for value in left_list:
        similarity_score += counter[value] * value
    return similarity_score

def main():
    parsed_input = parse_input_file("input.txt")
    input_lists = input_to_lists(parsed_input)

    part_1_result = total_list_distance(*input_lists)
    print(f"Part 1: {part_1_result}")

    part_2_result = similarity_score(*input_lists)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python

import os
import typing
import collections
import copy


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input


def get_reports(parsed_input: typing.List[str]) -> typing.List[typing.List[int]]:
    reports = []
    for row in parsed_input:
        reports.append([int(level) for level in row.split(" ")])
    return reports


def check_safety(
    report: typing.List[int],
    direction: bool = None,
) -> bool:
    if len(report) < 2:
        if direction is None:
            print("Invalid report")
            return None
        # Safe report
        return True

    current, *remainder = report
    next, *_ = remainder
    distance = abs(next - current)
    current_direction = next > current
    distance_ok = 1 <= distance <= 3
    direction_ok = (direction is None) or (current_direction == direction)
    valid_step = distance_ok and direction_ok

    return valid_step and check_safety(
        remainder,
        direction=current_direction,
    )


def check_safety_tolerant(report: typing.List[int]) -> bool:
    result = check_safety(report)
    if result:
        return result
    for index in range(0, len(report)):
        permutation = copy.copy(report)
        permutation.pop(index)
        result = check_safety(permutation)
        if result:
            return result
    return False


def count_safe_reports(reports: typing.List[int]) -> int:
    safety = collections.Counter([check_safety(report) for report in reports])
    return safety[True]


def count_safe_reports_tolerant(reports: typing.List[int]) -> int:
    safety = collections.Counter([check_safety_tolerant(report) for report in reports])
    return safety[True]


def main():
    parsed_input = parse_input_file("input.txt")
    reports = get_reports(parsed_input)

    part_1_result = count_safe_reports(reports)
    print(f"Part 1: {part_1_result}")

    part_2_result = count_safe_reports_tolerant(reports)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

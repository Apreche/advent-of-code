#!/usr/bin/env python

import collections
import math
import os


def straight_line_filter(lines):
    filtered_lines = []
    for line in lines:
        start, end = line
        is_vertical = start[0] == end[0]
        is_horizontal = start[1] == end[1]
        if is_vertical or is_horizontal:
            filtered_lines.append(line)
    return filtered_lines


def get_points_on_line(line):
    points = []
    start, end = line
    xdelta = end[0] - start[0]
    ydelta = end[1] - start[1]
    common_denominator = math.gcd(xdelta, ydelta)
    xslope = int(xdelta / common_denominator)
    yslope = int(ydelta / common_denominator)
    current_point = start
    while current_point != end:
        points.append(current_point)
        x, y = current_point
        current_point = (x + xslope, y + yslope)
    points.append(current_point)
    return points


def get_points_on_all_lines(lines):
    all_points = []
    for line in lines:
        all_points += get_points_on_line(line)
    return all_points


def find_colliding_points(points):
    colliding_points = []
    for point, count in collections.Counter(points).items():
        if count > 1:
            colliding_points.append(point)
    return colliding_points


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            raw_start, raw_end = tuple(line.split('->'))
            start = tuple([int(x) for x in raw_start.strip().split(',')])
            end = tuple([int(x) for x in raw_end.strip().split(',')])
            parsed_input.append((start, end))
    return parsed_input


def main():
    all_lines = parse_input_file("input.txt")
    filtered_lines = straight_line_filter(all_lines)

    all_points = get_points_on_all_lines(filtered_lines)
    colliding_points = find_colliding_points(all_points)

    part_1_result = len(colliding_points)
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

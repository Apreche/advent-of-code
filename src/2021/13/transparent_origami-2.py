#!/usr/bin/env python

import copy
import os
import re


class TransparentPaper:
    def __init__(self, dot_locations):
        self.locations = set(copy.deepcopy(dot_locations))

    def _fold_x(self, fold_point):
        newset = set()
        for location in self.locations:
            x, y = location
            if x > fold_point:
                fold_distance = (x - fold_point) * 2
                new_x = x - fold_distance
                newset.add((new_x, y))
            else:
                newset.add(location)
        self.locations = newset

    def _fold_y(self, fold_point):
        newset = set()
        for location in self.locations:
            x, y = location
            if y > fold_point:
                fold_distance = (y - fold_point) * 2
                new_y = y - fold_distance
                newset.add((x, new_y))
            else:
                newset.add(location)
        self.locations = newset

    def dot_count(self):
        return len(self.locations)

    def fold(self, dimension, point):
        if dimension == "x":
            self._fold_x(point)
        if dimension == "y":
            self._fold_y(point)

    def display(self):
        all_x = [x for x, y in self.locations]
        all_y = [y for x, y in self.locations]
        max_x = max(all_x)
        min_x = min(all_x)
        max_y = max(all_y)
        min_y = min(all_y)

        lines = []
        for y in range(min_y, max_y + 1):
            line = []
            for x in range(min_x, max_x + 1):
                if (x, y) in self.locations:
                    line.append("#")
                else:
                    line.append(".")
            lines.append("".join(line))
        print("\n".join(lines))


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        dot_locations = []
        line = input_file.readline()
        while line != "\n":
            dot_locations.append(
                tuple([int(n) for n in line.strip().split(',')])
            )
            line = input_file.readline()
        pattern = re.compile(
            r'^fold along ([xy])=(\d+)$'
        )
        folds = []
        for line in input_file.read().splitlines():
            match = pattern.match(line)
            folds.append(
                (match.group(1), int(match.group(2)))
            )
    return (dot_locations, folds)


def main():
    dot_locations, folds = parse_input_file("input.txt")
    paper = TransparentPaper(dot_locations)

    paper.fold(*folds[0])
    part_1_result = paper.dot_count()
    print(f"Part 1: {part_1_result}")

    paper = TransparentPaper(dot_locations)
    for fold in folds:
        paper.fold(*fold)
    print("Part 2:")
    paper.display()


if __name__ == "__main__":
    main()

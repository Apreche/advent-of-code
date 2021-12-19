#!/usr/bin/env python

import copy
import operator
import os
import re
from tqdm import tqdm

from dataclasses import dataclass
from typing import List


def triangular_number(x: int) -> int:
    """ Get the xth triangular number """
    return (x * (x + 1)) // 2


def minimum_triangular_number(minimum: int) -> int:
    """
    Find the smallest triangular number that is >= minimum
    Return which triangular number it is.

    e.g.: The smallest triangular number that's at least 11 is 15
    15 is the 5th triangular number, so return 5
    """
    val = 0
    count = 0
    while val < minimum:
        count += 1
        val = triangular_number(count)
    return count


@dataclass
class Vector:
    vx: int
    vy: int

    def step(self) -> None:
        if self.vx < 0:
            self.vx += 1
        elif self.vx > 0:
            self.vx -= 1
        self.vy -= 1

    @property
    def max_height(self) -> int:
        # Max height for part 1 is triangular number of vy
        return triangular_number(self.vy)


@dataclass
class Point:
    x: int
    y: int

    def move(self, vector: Vector) -> None:
        self.x += vector.vx
        self.y += vector.vy


@dataclass
class Target:
    minx: int
    maxx: int
    miny: int
    maxy: int

    def contains(self, point: Point) -> bool:
        """ Is the point on target? """
        x_in_range = self.minx <= point.x <= self.maxx
        y_in_range = self.miny <= point.y <= self.maxy
        return x_in_range and y_in_range

    def vxrange(self, origin: Point) -> range:
        """ What is the minimum vx worth checking? """
        if self.minx <= origin.x <= self.maxx:
            # We can shoot straight up in the air
            return range(0, 1)

        if origin.x < self.minx:
            # shoot right by default
            maxvx = -1 * (origin.x - self.maxx)
            distance_to_target = abs(origin.x - self.minx)
            minvx = minimum_triangular_number(distance_to_target)
            return range(minvx, maxvx + 1, 1)
        else:
            # shoot left
            minvx = -1 * (origin.x - self.minx)
            distance_to_target = abs(origin.x - self.maxx)
            maxvx = -1 * minimum_triangular_number(distance_to_target)
            return range(maxvx, minvx - 1, -1)

    def vyrange(self, origin: Point) -> range:
        # If box includes origin height, maxvy = infinity
        assert(not (self.miny <= origin.y <= self.maxy))

        # Find minvy
        distance_to_bottom = abs(origin.y - self.miny)
        if origin.y >= self.miny:
            minvy = -1 * abs(origin.y - self.miny)
        else:
            minvy = minimum_triangular_number(
                distance_to_bottom
            )

        # Find maxvy
        if origin.y >= self.maxy:
            maxvy = distance_to_bottom - 1
        else:
            maxvy = abs(self.maxy - origin.y)

        return range(minvy, maxvy + 1)


def fire_shot(origin: Point, vector: Vector,  target: Target):
    locations = []
    location = copy.copy(origin)
    shot = copy.copy(vector)
    hits = []
    while location.y >= target.miny:
        locations.append(copy.copy(location))
        location.move(shot)
        shot.step()
        if target.contains(location):
            hits.append(copy.copy(location))
    return hits


def hit_target(target: Target, origin: Point) -> List[Vector]:
    successful_shots = []
    for vy in tqdm(target.vyrange(origin)):
        for vx in target.vxrange(origin):
            shot = Vector(vx, vy)
            hits = fire_shot(origin, shot, target)
            if hits:
                successful_shots.append(shot)
    return successful_shots


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    input_pattern = r'^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$'
    with open(full_file_path) as input_file:
        line = input_file.readline()
        match = re.search(input_pattern, line)
    return Target(*[int(x) for x in match.groups()])


def main():
    target = parse_input_file("input.txt")
    origin = Point(0, 0)
    successful_shots = hit_target(target, origin)
    highest_shot = max(successful_shots, key=operator.attrgetter('vy'))

    part_1_result = highest_shot.max_height + origin.y
    print(f"Part 1: {part_1_result}")

    part_2_result = len(successful_shots)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

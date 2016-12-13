#!/usr/bin/env python

import operator

with open('input.txt', 'r') as input_file:
    raw_directions = input_file.read().replace('\n', '')

directions = raw_directions.split(', ')

directions_map = {
    'N': {'L': 'W', 'R': 'E', 'delta': (0, 1)},
    'S': {'L': 'E', 'R': 'W', 'delta': (0, -1)},
    'E': {'L': 'N', 'R': 'S', 'delta': (1, 0)},
    'W': {'L': 'S', 'R': 'N', 'delta': (-1, 0)},
}

current_direction = 'N'
current_coordinates = (0, 0)

coordinate_history = [current_coordinates]

answer_2_location = None

for direction in directions:
    movement = direction[0]
    steps = int(direction[1:])

    current_direction = directions_map[current_direction][movement]
    delta = directions_map[current_direction]['delta']

    for step in range(steps):
        current_coordinates = tuple(map(operator.add, current_coordinates,
                                        delta))
        if answer_2_location is None:
            if current_coordinates in coordinate_history:
                answer_2_location = current_coordinates
            else:
                coordinate_history.append(current_coordinates)


answer_1 = sum([abs(x) for x in current_coordinates])
answer_2 = sum([abs(x) for x in answer_2_location])


print "PART 1: %s" % answer_1
print "PART 2: %s" % answer_2

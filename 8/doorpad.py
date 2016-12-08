#!/usr/bin/env python
import re
from display import Display

instructions = []
with open('input.txt', 'r') as input_file:
    for instruction in input_file:
        instruction = instruction.replace('\n', '')
        instructions.append(instruction)

screen = Display(50, 6)

rect_pattern = re.compile(r'^rect (\d+)x(\d+)$')
rotate_row_pattern = re.compile(r'^rotate row y=(\d+) by (\d+)')
rotate_column_pattern = re.compile(r'^rotate column x=(\d+) by (\d+)')

for instruction in instructions:
    rect_match = rect_pattern.match(instruction)
    if rect_match is not None:
        width, height = rect_match.groups()
        screen.rect(int(width), int(height))
        continue

    row_match = rotate_row_pattern.match(instruction)
    if row_match is not None:
        row, distance = row_match.groups()
        screen.rotate_row(int(row), int(distance))
        continue

    column_match = rotate_column_pattern.match(instruction)
    if column_match is not None:
        column, distance = column_match.groups()
        screen.rotate_column(int(column), int(distance))
        continue

print "ANSWER 1: %s\n" % screen.count
print "ANSWER 2: \n"
print screen
print ""

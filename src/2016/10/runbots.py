#!/usr/bin/env python
import re
from bots import Factory

input_pattern = re.compile(r'^value (\d+) goes to bot (\d+)$')
p2 = r'^bot (\d+) gives (low|high) to (bot|output) (\d+) and (high|low) to (bot|output) (\d+)$'
instruction_pattern = re.compile(p2)

instructions = []
factory = Factory()

with open('input.txt', 'r') as input_file:
    for line in input_file:
        line = line.strip()
        match = input_pattern.search(line)
        if match is not None:
            value, bot_id = match.groups()
            factory.input(int(bot_id), int(value))
            continue
        match = instruction_pattern.search(line)
        if match is not None:
            instructions.append(match.groups())
            continue


while instructions:
    for instruction in instructions:
        from_id, from1, to1, to1_id, from2, to2, to2_id = instruction
        from_id = int(from_id)
        to1_id = int(to1_id)
        to2_id = int(to2_id)
        result = factory.instruct(from_id, from1, to1, to1_id)
        if result:
            result = factory.instruct(from_id, from2, to2, to2_id)
            instructions.remove(instruction)

print factory

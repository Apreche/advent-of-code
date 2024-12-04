#!/usr/bin/env python

import copy
import hgc


def parse_input_file(filename: str):
    with open(filename) as input_file:
        program = []
        for line in input_file.read().splitlines():
            instruction, param = line.split(' ')
            program.append((instruction, int(param)))
    return program


def fix_program(program_listing):
    flipper = {
        'nop': 'jmp',
        'jmp': 'nop',
    }

    for line_no, instruction in enumerate(program_listing):
        command, param = instruction
        if command not in flipper:
            continue
        new_listing = copy.copy(program_listing)
        new_listing[line_no] = (flipper[command], param)
        handheld_game = hgc.HGC()
        completed, part_2_result = handheld_game.execute(
            new_listing
        )
        if completed:
            return part_2_result


def main():
    program_listing = parse_input_file('input.txt')
    handheld_game = hgc.HGC()
    completed, part_1_result = handheld_game.execute(
        program_listing
    )
    print(f"Part 1: {part_1_result}")

    part_2_result = fix_program(program_listing)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

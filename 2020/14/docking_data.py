#!/usr/bin/env python

import copy
import re


def parse_input_file(filename: str):

    mask_regex = r'^mask = ([10X]{36})$'
    mem_regex = r'^mem\[([0-9]+)\] = ([0-9]+)$'

    with open(filename) as input_file:

        parsed_input = []
        for line in input_file.read().splitlines():
            mask_match = re.search(mask_regex, line)
            mem_match = re.search(mem_regex, line)
            if mask_match:
                parsed_input.append(
                    ('MASK', mask_match.groups()[0])
                )
            else:  # mem match
                parsed_input.append(
                    (
                        'MEM',
                        int(mem_match.groups()[0]),
                        int(mem_match.groups()[1]),
                    )
                )
    return parsed_input


class DockingCPU:
    def __init__(self, instructions):
        self.instructions = instructions
        self.mask = None
        self.memory = {}

    def _setmask(self, mask):
        self.mask = mask

    def _apply_mask(self, value, v2=False):
        if not self.mask:
            raise Exception("No Mask Set")
        binvalue = format(value, '#038b')[2:]
        binlist = [x for x in binvalue]
        for index, digit in enumerate(self.mask):
            if v2:
                if digit == '1':
                    binlist[index] = digit
                elif digit == 'X':
                    binlist[index] = 'X'
            else:
                if digit != 'X':
                    binlist[index] = digit
        return binlist

    def _setmem(self, location, value):
        binlist = self._apply_mask(value)
        self.memory[location] = int(''.join(binlist), 2)

    def _setmemv2(self, location, value):
        masked_mem = self._apply_mask(location, v2=True)

        mem_location_set = []
        num_xs = masked_mem.count('X')
        num_masks = 2 ** num_xs
        for mask_num in range(num_masks):
            fnum = num_xs + 2
            x_bits = format(mask_num, f'#0{fnum}b')[2:]
            mlist = copy.copy(masked_mem)
            for bit in x_bits:
                mlist[mlist.index('X')] = bit
            mem_location_set.append(
                int(''.join(mlist), 2)
            )

        for mem_location in mem_location_set:
            self.memory[mem_location] = value

    def memsum(self):
        return sum(self.memory.values())

    def execute(self, v2=False):
        setmem = self._setmem
        if v2:
            setmem = self._setmemv2
        for instruction in self.instructions:
            if instruction[0] == 'MASK':
                self._setmask(instruction[1])
            else:
                setmem(
                    instruction[1],
                    instruction[2],
                )


def main():
    parsed_input = parse_input_file("input.txt")
    cpu = DockingCPU(parsed_input)
    cpu.execute()

    part_1_result = cpu.memsum()
    print(f"Part 1: {part_1_result}")

    cpu = DockingCPU(parsed_input)
    cpu.execute(v2=True)
    part_2_result = cpu.memsum()
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python

from bitarray import bitarray, util
import math
import os


class Packet:

    SUM_PACKET_TYPE_ID = 0
    PRODUCT_PACKET_TYPE_ID = 1
    MIN_PACKET_TYPE_ID = 2
    MAX_PACKET_TYPE_ID = 3
    LITERAL_PACKET_TYPE_ID = 4
    GT_PACKET_TYPE_ID = 5
    LT_PACKET_TYPE_ID = 6
    EQ_PACKET_TYPE_ID = 7

    TOTAL_LENGTH_TYPE_ID = 0
    NUMBER_LENGTH_TYPE_ID = 1

    VALUE_OPERATORS = {
        SUM_PACKET_TYPE_ID: sum,
        PRODUCT_PACKET_TYPE_ID: math.prod,
        MIN_PACKET_TYPE_ID: min,
        MAX_PACKET_TYPE_ID: max,
    }

    def __init__(self, bits: bitarray) -> None:
        self.original_bits = bits
        self.version = util.ba2int(bits[:3])
        self.packet_type_id = util.ba2int(bits[3:6])
        self.literal_value = None
        self.length_type_id = None
        self.children = []
        self.extra_bits = bitarray()
        self._parse_packet(bits[6:])

    def __repr__(self) -> str:
        if self.packet_type_id == self.LITERAL_PACKET_TYPE_ID:
            return f"Packet: v{self.version} - Literal {self.literal_value}"
        else:
            num_children = len(self.children)
            return f"Packet: v{self.version} - T{self.length_type_id} - C{num_children}"

    def _parse_packet(self, bits: bitarray) -> None:
        """ Choose a parsing method for this packet """
        if self.packet_type_id == self.LITERAL_PACKET_TYPE_ID:
            self._parse_literal(bits)
        else:
            self.length_type_id = bits[0]
            if self.length_type_id == self.TOTAL_LENGTH_TYPE_ID:
                self._parse_total_children(bits[1:])
            elif self.length_type_id == self.NUMBER_LENGTH_TYPE_ID:
                self._parse_number_children(bits[1:])

    def _parse_literal(self, bits: bitarray) -> None:
        """ Parse packet as a literal value """
        literal = bitarray()
        stop_bit = 1
        index = 0
        while stop_bit == 1:
            stop_bit = bits[index]
            literal += bits[index+1:index+5]
            index += 5
        self.literal_value = util.ba2int(literal)
        self.extra_bits = bits[index:]

    def _parse_total_children(self, bits: bitarray) -> None:
        """ Parse packet as total length type """
        child_data_length = util.ba2int(bits[:15])
        child_bits = bits[15:15+child_data_length]
        while any(child_bits):
            new_child = Packet(child_bits)
            self.children.append(new_child)
            child_bits = new_child.extra_bits
        self.extra_bits = bits[15+child_data_length:]

    def _parse_number_children(self, bits: bitarray) -> None:
        """ Parse packet as packet number type """
        packet_count = util.ba2int(bits[:11])
        child_bits = bits[11:]
        for _ in range(packet_count):
            new_child = Packet(child_bits)
            self.children.append(new_child)
            child_bits = new_child.extra_bits
        self.extra_bits = child_bits

    def total_version_number(self) -> int:
        """ Total version numbers for self and all child packets """
        version = self.version
        version += sum([c.total_version_number() for c in self.children])
        return version

    def value(self) -> int:
        """ Return the value of the packet as defined in Part 2"""
        if self.packet_type_id == self.LITERAL_PACKET_TYPE_ID:
            return self.literal_value

        child_values = [c.value() for c in self.children]

        if self.packet_type_id in self.VALUE_OPERATORS:
            return self.VALUE_OPERATORS[self.packet_type_id](child_values)
        elif self.packet_type_id == self.GT_PACKET_TYPE_ID:
            return int(child_values[0] > child_values[1])
        elif self.packet_type_id == self.LT_PACKET_TYPE_ID:
            return int(child_values[0] < child_values[1])
        elif self.packet_type_id == self.EQ_PACKET_TYPE_ID:
            return int(child_values[0] == child_values[1])


def parse_input_file(filename: str) -> bitarray:
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    parsed_input = None
    with open(full_file_path) as input_file:
        parsed_input = input_file.readline().strip()
    return util.hex2ba(parsed_input)


def main() -> None:
    parsed_input = parse_input_file("input.txt")
    packet = Packet(parsed_input)

    part_1_result = packet.total_version_number()
    print(f"Part 1: {part_1_result}")

    part_2_result = packet.value()
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

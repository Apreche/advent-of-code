#!/usr/bin/env python

import os


class Decoder:

    def __init__(self, sample, display):
        self.sample = sample
        self.display = display
        self._decode()

    def _disambiguate_sixlen(self, digit, present_char, missing_char):
        assert(digit in [0, 6, 9])
        candidates = self.letter_map[present_char]
        for code in self.sample:
            if len(code) == 6 and (not candidates.issubset(code)):
                self.digit_map[digit] = set(code)

        for character in candidates:
            if character in self.digit_map[digit]:
                self.letter_map[present_char] = {character}
            else:
                self.letter_map[missing_char] = {character}

    def _disambiguate_twofive(self, digit, character):
        assert(digit in [2, 5])
        candidates = self.letter_map[character]
        for code in self.sample:
            if len(code) == 5 and candidates.issubset(code):
                self.digit_map[digit] = set(code)

    def _decode(self):
        self.digit_map = {}
        self.letter_map = {}
        finder = {
            1: 2,
            4: 4,
            7: 3,
            8: 7
        }
        for digit, count in finder.items():
            for code in self.sample:
                if len(code) == count:
                    self.digit_map[digit] = set(code)

        self.letter_map['a'] = self.digit_map[7] - self.digit_map[1]
        self.letter_map['b'] = self.digit_map[4] - self.digit_map[7]
        self.letter_map['c'] = self.digit_map[1]
        self.letter_map['d'] = self.digit_map[4] - self.digit_map[7]
        self.letter_map['e'] = self.digit_map[8] - self.digit_map[7].union(
            self.digit_map[4]
        )
        self.letter_map['f'] = self.digit_map[1]
        self.letter_map['g'] = self.digit_map[8] - self.digit_map[7].union(
            self.digit_map[4]
        )

        self._disambiguate_sixlen(6, 'f', 'c')
        self._disambiguate_sixlen(0, 'b', 'd')
        self._disambiguate_sixlen(9, 'g', 'e')
        self._disambiguate_twofive(2, 'e')
        self._disambiguate_twofive(5, 'b')

        self.digit_map[3] = set({}).union(
            self.letter_map['a'],
            self.letter_map['c'],
            self.letter_map['d'],
            self.letter_map['f'],
            self.letter_map['g'],
        )

    def count_digits(self, digits):
        counter = 0
        for digit in digits:
            for display_digit in self.display:
                if self.digit_map[digit] == set(display_digit):
                    counter += 1
        return counter


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            raw_sample, raw_display = (
                text.strip() for text in line.split('|')
            )
            parsed_input.append(
                (raw_sample.split(), raw_display.split())
            )
    return parsed_input


def main():
    parsed_input = parse_input_file("input.txt")
    decoders = []
    for sample, display in parsed_input:
        decoders.append(Decoder(sample, display))

    part_1_result = sum(
        [decoder.count_digits([1, 4, 7, 8]) for decoder in decoders]
    )
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

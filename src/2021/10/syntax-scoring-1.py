#!/usr/bin/env python

import os


class SyntaxStack:
    OPENING_CHARS = "([{<"
    CLOSING_CHARS = ")]}>"

    CHAR_PAIRS = {
        '{': '}',
        '}': '{',
        '(': ')',
        ')': '(',
        '[': ']',
        ']': '[',
        '<': '>',
        '>': '<',
    }

    SCORES = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    def __init__(self, line):
        self.line = line
        self.illegal_char = None
        self.stack = []
        self._check_syntax()

    def _check_syntax(self):
        for char in self.line:
            if char in self.OPENING_CHARS:
                self.stack.append(char)
            if char in self.CLOSING_CHARS:
                if self.CHAR_PAIRS[self.stack.pop()] != char:
                    self.illegal_char = char
                    return False
        return True

    @property
    def is_legal(self):
        return self.illegal_char is None

    @property
    def score(self):
        if self.illegal_char is None:
            return 0
        else:
            return self.SCORES[self.illegal_char]


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input


def main():
    parsed_input = parse_input_file("input.txt")
    stacks = [SyntaxStack(line) for line in parsed_input]

    part_1_result = sum([stack.score for stack in stacks])
    print(f"Part 1: {part_1_result}")

    part_2_result = None
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

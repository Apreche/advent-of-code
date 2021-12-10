#!/usr/bin/env python

import copy
import statistics
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

    INCOMPLETE_SCORES = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    ILLEGAL_SCORES = {
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
    def illegal_score(self):
        if self.illegal_char is None:
            return 0
        else:
            return self.ILLEGAL_SCORES[self.illegal_char]

    @property
    def incomplete_score(self):
        stack = copy.copy(self.stack)
        score = 0
        if self.illegal_char is not None:
            return score
        while stack:
            char = self.CHAR_PAIRS[stack.pop()]
            score = int(score * 5)
            score += self.INCOMPLETE_SCORES[char]
        return score


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

    part_1_result = sum([stack.illegal_score for stack in stacks])
    print(f"Part 1: {part_1_result}")

    incomplete_scores = [stack.incomplete_score for stack in stacks]
    part_2_scores = [score for score in incomplete_scores if score != 0]
    part_2_result = statistics.median(part_2_scores)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python

class GravityMachine:

    def add(self):
        left_position = self.program[self.position + 1]
        right_position = self.program[self.position + 2]
        result_position = self.program[self.position + 3]
        self.program[result_position] = self.program[left_position] + self.program[right_position]

    def multiply(self):
        left_position = self.program[self.position + 1]
        right_position = self.program[self.position + 2]
        result_position = self.program[self.position + 3]
        self.program[result_position] = self.program[left_position] * self.program[right_position]

    OPCODES = {
        1: add,
        2: multiply,
        99: 99,
    }

    def __init__(self, program_text):
        self.original_program = [int(x) for x in program_text.split(',')]
        self.reset()

    def set(self, position, value):
        self.program[position] = value

    def get(self, position):
        return self.program[position]

    def reset(self):
        self.position = 0
        self.program = self.original_program.copy()

    def execute(self):
        while self.position < len(self.program):
            instruction = self.program[self.position]
            operation = self.OPCODES.get(instruction, None)
            if operation in [99, None]:
                if operation is None:
                    print(f"Invalid OPCODE {instruction}")
                break
            else:
                operation(self)
                self.position += 4

def generate_pairs():
    for noun in range(100):
        for verb in range(100):
            yield noun, verb

if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        input_program = input_file.read()
    machine = GravityMachine(input_program)

    for noun, verb in generate_pairs():
        machine.reset()
        machine.set(1, noun)
        machine.set(2, verb)
        machine.execute()
        result = machine.get(0)
        if result == 19690720:
            print(f"NOUN - {noun}")
            print(f"VERB - {verb}")

            answer = 100 * noun + verb
            print(f"ANSWER - {answer}")
            break

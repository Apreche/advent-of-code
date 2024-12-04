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
        print(f"DONE - {self.position}")
        print(self.program)

if __name__ == "__main__":
    with open('input.txt', 'r') as input_file:
        input_program = input_file.read()
    machine = GravityMachine(input_program)
    machine.set(1, 12)
    machine.set(2, 2)
    machine.execute()
    result = machine.get(0)
    print(f"Position 0 = {result}")

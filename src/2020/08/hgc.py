class HGC:
    # Handheld Gaming Computer

    def __init__(self):
        self.boot()

    def boot(self):
        self.program_counter = 0
        self.accumulator = 0

    def execute(self, program):

        instruction_set = {
            'jmp': self.jump,
            'nop': self.no_operation,
            'acc': self.accumulate,
        }

        executed_instructions = []

        while 0 <= self.program_counter < len(program):
            instruction, param = program[
                self.program_counter
            ]

            if self.program_counter in executed_instructions:
                return (False, self.accumulator)

            executed_instructions.append(
                self.program_counter
            )
            instruction_set[instruction](param)

        if self.program_counter == len(program):
            return (True, self.accumulator)
        else:
            return (None, self.accumulator)

    def jump(self, param):
        self.program_counter += param

    def no_operation(self, *args):
        self.jump(1)

    def accumulate(self, param):
        self.accumulator += param
        self.jump(1)

#!/usr/bin/env python

DIGITS = [str(x) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
OPERATORS = {
    '+': 2,
    '*': 1,
}


def parse_input_file(filename: str):
    with open(filename) as input_file:
        return input_file.read().splitlines()


def rpn_convert(problem):
    problem = problem.replace(' ', '')
    output_queue = []
    operator_stack = []

    for char in problem:
        if char in DIGITS:
            output_queue.append(int(char))
        elif char in OPERATORS:
            while (
                operator_stack and (
                    operator_stack[-1] in OPERATORS
                )
            ):
                output_queue.append(operator_stack.pop())
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and (operator_stack[-1] != '('):
                output_queue.append(operator_stack.pop())
            if operator_stack and (operator_stack[-1] == '('):
                operator_stack.pop()
    while operator_stack:
        output_queue.append(operator_stack.pop())
    return output_queue


def rpn_convert2(problem):
    problem = problem.replace(' ', '')
    output_queue = []
    operator_stack = []

    for char in problem:
        if char in DIGITS:
            output_queue.append(int(char))
        elif char in OPERATORS:
            while (
                operator_stack and (
                    operator_stack[-1] in OPERATORS
                ) and (
                    OPERATORS[operator_stack[-1]] >= OPERATORS[char]
                )
            ):
                output_queue.append(operator_stack.pop())
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and (operator_stack[-1] != '('):
                output_queue.append(operator_stack.pop())
            if operator_stack and (operator_stack[-1] == '('):
                operator_stack.pop()
    while operator_stack:
        output_queue.append(operator_stack.pop())
    return output_queue


def rpn_eval(rpn):
    stack = []

    for token in rpn:
        if token in OPERATORS:
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = eval(f"{arg1} {token} {arg2}")
            stack.append(result)
        else:
            stack.append(token)

    return stack.pop()


def solve_part_one(problems=[]):
    answer = 0
    for problem in problems:
        answer += rpn_eval(rpn_convert(problem))
    return answer


def solve_part_two(problems=[]):
    answer = 0
    for problem in problems:
        answer += rpn_eval(rpn_convert2(problem))
    return answer


def main():
    test_input = [
        ('1 + (2 * 3) + (4 * (5 + 6))', 51, 51),
        ('2 * 3 + (4 * 5)', 26, 46),
        ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437, 1445),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240, 669060),
        ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632, 23340),
    ]
    for test, answer1, answer2 in test_input:
        result1 = rpn_eval(rpn_convert(test))
        assert(result1 == answer1)
        result2 = rpn_eval(rpn_convert2(test))
        assert(result2 == answer2)

    real_input = parse_input_file("input.txt")

    part_1_result = solve_part_one(real_input)
    print(f"Part 1: {part_1_result}")

    part_2_result = solve_part_two(real_input)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

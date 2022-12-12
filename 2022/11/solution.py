#!/usr/bin/env python

import math
import operator
import os
import re


class Monkey:
    def __init__(self, definition=[], less_worried=True, lcm=1):
        start, operation, test, success, fail = definition
        self._set_start(start)
        self._set_operation(operation)
        self._set_test(test)
        self._set_success(success)
        self._set_fail(fail)
        self.num_inspections = 0
        self.lcm = lcm
        self.less_worried = less_worried

    def _set_start(self, start_str):
        header, values = start_str.split(": ")
        assert (header == "Starting items")
        self.items = [int(n) for n in values.split(", ")]

    def _set_operation(self, operation_str):
        header, values = operation_str.split(": ")
        assert (header == "Operation")
        pattern = re.compile(r"^new = (.*)$")
        result = pattern.match(values)
        assert (result is not None)
        assert (hasattr(result, "groups"))
        operation_parts = result.groups()[0].split(" ")
        assert (len(operation_parts) == 3)
        left, str_operator, right = operation_parts
        if left.isnumeric():
            self.left_operand = int(left)
        else:
            self.left_operand = "old"
        if right.isnumeric():
            self.right_operand = int(right)
        else:
            self.right_operand = "old"
        assert (str_operator in ["+", "*"])
        self.str_operator = str_operator

    def _set_test(self, test_str):
        header, values = test_str.split(": ")
        assert (header == "Test")
        pattern = re.compile(r"^divisible by (\d+)$")
        result = pattern.match(values)
        assert (result is not None)
        assert (hasattr(result, "groups"))
        self.test_val = int(result.groups()[0])

    def _set_success(self, success_str):
        header, values = success_str.split(": ")
        assert (header == "If true")
        pattern = re.compile(r"^throw to monkey (\d+)$")
        result = pattern.match(values)
        assert (result is not None)
        assert (hasattr(result, "groups"))
        self.success_val = int(result.groups()[0])

    def _set_fail(self, fail_str):
        header, values = fail_str.split(": ")
        assert (header == "If false")
        pattern = re.compile(r"^throw to monkey (\d+)$")
        result = pattern.match(values)
        assert (result is not None)
        assert (hasattr(result, "groups"))
        self.fail_val = int(result.groups()[0])

    def operate(self, item):
        operations = {
            "+": operator.add,
            "*": operator.mul,
        }
        operation = operations[self.str_operator]
        left_operand, right_operand = item, item
        if isinstance(self.left_operand, int):
            left_operand = self.left_operand
        if isinstance(self.right_operand, int):
            right_operand = self.right_operand
        return operation(left_operand, right_operand)

    def test(self, worry_level):
        result = (worry_level % self.test_val) == 0
        return result

    def throw_item(self, item):
        worry_level = self.operate(item)
        self.num_inspections += 1
        if self.less_worried:
            worry_level = worry_level // 3
        else:
            worry_level = worry_level % self.lcm
        test_result = self.test(worry_level)
        throw_to = self.fail_val
        if test_result:
            throw_to = self.success_val
        return (throw_to, worry_level)

    def throw_all(self):
        results = []
        num_items = len(self.items)
        for i, item in enumerate(self.items):
            results.append(
                self.throw_item(item)
            )
        self.items = []
        return results

    def catch_item(self, item):
        self.items.append(item)


def parse_input_file(filename: str):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        monkeys = []
        monkey = []
        for line in input_file.read().splitlines():
            if line:
                monkey.append(line.strip())
            else:
                monkeys.append(monkey)
                monkey = []
        monkeys.append(monkey)
    return monkeys


def make_monkeys(monkey_definitions, less_worried=True):
    monkeys = []
    for definition in monkey_definitions:
        monkeys.append(
            Monkey(
                definition=definition[1:],
                less_worried=less_worried,
            )
        )
    # Once we have all the monkeys, go back and set their lcm
    lcm = math.lcm(*[monkey.test_val for monkey in monkeys])
    for monkey in monkeys:
        monkey.lcm = lcm
    return monkeys


def simulate_monkeys(monkeys, rounds=20):
    for i in range(rounds):
        for mi, monkey in enumerate(monkeys):
            throws = monkey.throw_all()
            for destination, value in throws:
                monkeys[destination].catch_item(value)


def calculate_monkey_business(monkeys):
    inspections = [m.num_inspections for m in monkeys]
    most_active = sorted(inspections, reverse=True)[:2]
    return math.prod(most_active)


def main():
    monkey_definitions = parse_input_file("input.txt")
    monkeys = make_monkeys(monkey_definitions)
    simulate_monkeys(monkeys)

    part_1_result = calculate_monkey_business(monkeys)
    print(f"Part 1: {part_1_result}")

    monkeys = make_monkeys(
        monkey_definitions,
        less_worried=False,
    )
    simulate_monkeys(monkeys, rounds=10000)

    part_2_result = calculate_monkey_business(monkeys)
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

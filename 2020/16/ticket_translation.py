#!/usr/bin/env python

import math
import re


def parse_input_file(filename: str):

    with open(filename) as input_file:

        all_lines = input_file.read().splitlines()

        rule_lines = all_lines[0:all_lines.index('')]
        rules = {}
        rule_regex = r'^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$'
        for line in rule_lines:
            name, min1, max1, min2, max2 = re.match(
                rule_regex, line
            ).groups()
            rules[name] = (
                int(min1),
                int(max1),
                int(min2),
                int(max2)
            )

        my_ticket_line = all_lines[all_lines.index('your ticket:') + 1]
        my_ticket = [int(x) for x in my_ticket_line.split(',')]

        nearby_ticket_lines = all_lines[all_lines.index('nearby tickets:') + 1:]
        nearby_tickets = []
        for line in nearby_ticket_lines:
            ticket = [int(x) for x in line.split(',')]
            nearby_tickets.append(ticket)

    return (rules, my_ticket, nearby_tickets)


def check_rule(rule, val):
    min1, max1, min2, max2 = rule
    first_range = (min1 <= val <= max1)
    second_range = (min2 <= val <= max2)
    return first_range or second_range


def check_all_rules(rules, val):
    checks = []
    for rule_name, rule in rules.items():
        checks.append(check_rule(rule, val))
    return any(checks)


def get_error_rate(rules, tickets=[]):
    error_rate = 0
    for ticket in tickets:
        for val in ticket:
            result = check_all_rules(rules, val)
            if not result:
                error_rate += val
    return error_rate


def remove_bad_tickets(rules, tickets=[]):
    good_tickets = []
    for ticket in tickets:
        valid = True
        for val in ticket:
            result = check_all_rules(rules, val)
            if not result:
                valid = False
                break
        if valid:
            good_tickets.append(ticket)
    return good_tickets


def get_possible_columns(rule, good_tickets):
    possible_columns = []
    for i in range(len(good_tickets[0])):
        could_match = True
        for ticket in good_tickets:
            result = check_rule(rule, ticket[i])
            if not result:
                could_match = False
                break
        if could_match:
            possible_columns.append(i)
    return possible_columns


def find_set_columns(possibilities):
    found_columns = []
    for name, indices in possibilities.items():
        if len(indices) == 1:
            found_columns.append(indices[0])
    return found_columns


def get_correct_columns(rules, good_tickets):
    all_possibilities = {}
    for name, rule in rules.items():
        all_possibilities[name] = get_possible_columns(
            rule, good_tickets
        )

    found_columns = []
    while len(found_columns) < len(rules):
        found_columns = find_set_columns(all_possibilities)
        for name in all_possibilities:
            if len(all_possibilities[name]) > 1:
                for col in found_columns:
                    if col in all_possibilities[name]:
                        all_possibilities[name].remove(col)
    return all_possibilities


def process_part_2(my_ticket, correct_columns):
    vals = []
    for name, indx in correct_columns.items():
        if name.startswith('departure'):
            i = indx[0]
            vals.append(my_ticket[i])
    return math.prod(vals)


def main():
    rules, my_ticket, nearby_tickets = parse_input_file(
        "input.txt"
    )

    part_1_result = get_error_rate(rules, nearby_tickets)
    print(f"Part 1: {part_1_result}")

    good_tickets = remove_bad_tickets(
        rules, nearby_tickets
    )
    good_tickets.append(my_ticket)
    correct_columns = get_correct_columns(
        rules, good_tickets
    )

    part_2_result = process_part_2(
        my_ticket,
        correct_columns
    )
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

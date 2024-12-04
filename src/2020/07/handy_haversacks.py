#!/usr/bin/env python

import re


def parse_input_file(filename: str):

    outer_regex = r'^([a-z]+) ([a-z]+) bags contain (.*)$'
    inner_regex = r'^(\d) ([a-z]+) ([a-z]+) bags?$'

    parsed_rules = {}
    parsed_rules_without_quantities = {}

    with open(filename) as input_file:

        for line in input_file.read().splitlines():

            parsed_rule = re.search(
                outer_regex, line
            ).groups()

            adjective, color, inner_string = parsed_rule
            outer_bag = (adjective, color)
            inner_bag_strings = inner_string[0:-1].split(', ')

            qty_inner_bags = {}
            no_qty_inner_bags = []

            if inner_string != 'no other bags.':
                for inner_bag_string in inner_bag_strings:
                    parsed_inner_bag = re.search(
                        inner_regex, inner_bag_string
                    ).groups()
                    quantity, adjective, color = parsed_inner_bag
                    inner_bag = (adjective, color)
                    qty_inner_bags[inner_bag] = int(quantity)
                    no_qty_inner_bags.append(inner_bag)

            parsed_rules[outer_bag] = qty_inner_bags
            parsed_rules_without_quantities[outer_bag] = no_qty_inner_bags

    return (parsed_rules, parsed_rules_without_quantities)


def get_containing_bags(rules, bag):
    outer_bags = []
    for outer_bag, inner_bags in rules.items():
        if bag in inner_bags:
            outer_bags.append(outer_bag)
            outer_bags += get_containing_bags(
                rules, outer_bag
            )
    return list(set(outer_bags))


def count_contained_bags(rules, bag):
    bag_count = 0
    current_rule = rules[bag]
    bag_count += sum(current_rule.values())
    for bag, quantity in current_rule.items():
        bag_count += count_contained_bags(rules, bag) * quantity
    return bag_count


def main():
    BAG = ('shiny', 'gold')
    rules, rules_no_qty = parse_input_file('input.txt')

    part_1_bags = get_containing_bags(
        rules_no_qty, BAG
    )
    part_1_result = len(part_1_bags)
    print(f"Part 1: {part_1_result}")

    part_2_result = count_contained_bags(
        rules, BAG
    )
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

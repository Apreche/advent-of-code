#!/usr/bin/env python

import regex


def parse_input_file(filename: str):

    with open(filename) as input_file:

        lines = input_file.read().splitlines()
        split_point = lines.index('')
        messages = lines[split_point+1:]
        unparsed_rules = lines[0:split_point]
        rules = {}
        for raw_rule in unparsed_rules:
            rule_id, rule_string = raw_rule.split(': ')
            rule_string = rule_string.replace('"', '')
            rule_list = rule_string.split(' ')
            parsed_rule_list = []
            for rule_item in rule_list:
                try:
                    parsed_rule_list.append(int(rule_item))
                except ValueError:
                    parsed_rule_list.append(rule_item)
            rules[int(rule_id)] = parsed_rule_list
    return rules, messages


def has_numbers(rule):
    return any([type(x) == int for x in rule])


def resolve_rules(rules, pre_resolved={}):
    resolved_rules = pre_resolved
    while len(resolved_rules) < len(rules):
        for rule_id, rule in rules.items():
            if has_numbers(rule) and any(
                item in resolved_rules for item in rule
            ):
                new_val = []
                for rule_part in rule:
                    if type(rule_part) == int:
                        if rule_part in resolved_rules:
                            replace_rule = resolved_rules[rule_part]
                            if '|' in replace_rule:
                                new_val.append('(')
                            new_val.append(
                                resolved_rules[rule_part]
                            )
                            if '|' in replace_rule:
                                new_val.append(')')
                        else:
                            new_val.append(rule_part)
                    else:
                        new_val.append(rule_part)
                rules[rule_id] = new_val
            elif not has_numbers(rule):
                if rule_id not in resolved_rules:
                    resolved_rules[rule_id] = ''.join(rule)
    regex_rules = {}
    for rule_id, rule in resolved_rules.items():
        regex_rule = r"^{}$".format(rule)
        regex_rules[rule_id] = regex_rule
    return regex_rules


def count_rule_matches(regex_rule, messages):
    match = [
        bool(regex.search(regex_rule, m)) for m in messages
    ]
    return len([x for x in match if x])


def main():
    rules, messages = parse_input_file("input.txt")
    regex_rules = resolve_rules(rules)

    part_1_result = count_rule_matches(
        regex_rules[0], messages
    )
    print(f"Part 1: {part_1_result}")

    # modify rules for part 2
    mod8 = r"({})+".format(
            regex_rules[8][1:-1]
    )
    mod42 = r'({})'.format(regex_rules[42][1:-1])
    mod31 = r'({})'.format(regex_rules[31][1:-1])
    group_num = mod8.count('(') + 3
    mod11 = r'({}(?{})*{})'.format(
        mod42, group_num, mod31
    )
    mod0 = r'^({})({})$'.format(mod8, mod11)
    part_2_result = count_rule_matches(
        mod0, messages
    )
    print(f"Part 2: {part_2_result}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
import re

addresses = []
with open('input.txt', 'r') as input_file:
    for address in input_file:
        addresses.append(address)


def contains_abba(string):
    for i in range(4, len(string) + 1):
        fragment = string[i-4:i]
        if all([fragment[0] == fragment[3],
                fragment[1] == fragment[2],
                fragment[0] != fragment[1]]):
            return True
    return False


all_pattern = re.compile(r'([a-z]+)')
bad_pattern = re.compile(r'\[([a-z]+)\]')

answer_1_count = 0
for address in addresses:
    bad_strings = bad_pattern.findall(address)
    if any([contains_abba(x) for x in bad_strings]):
        continue

    all_strings = all_pattern.findall(address)
    good_strings = [s for s in all_strings if s not in bad_strings]
    if any([contains_abba(x) for x in good_strings]):
        answer_1_count += 1

print "ANSWER 1: %s" % answer_1_count


def get_reverse_abas(string):
    abas = []
    for i in range(3, len(string) + 1):
        fragment = string[i-3:i]
        if all([fragment[0] == fragment[2],
                fragment[0] != fragment[1]]):
            abas.append(fragment)
    reverse_abas = []
    for aba in abas:
        reverse_abas.append(aba[1] + aba[0] + aba[1])
    return reverse_abas


def list_contains_aba(string_list, abas):
    for string in string_list:
        for aba in abas:
            result = string.find(aba)
            if result != -1:
                return True
    return False

answer_2_count = 0
for address in addresses:
    bad_strings = bad_pattern.findall(address)
    all_strings = all_pattern.findall(address)
    good_strings = [s for s in all_strings if s not in bad_strings]

    abas = []
    for string in good_strings:
        abas += get_reverse_abas(string)
    if not abas:
        continue
    else:
        if list_contains_aba(bad_strings, abas):
            answer_2_count += 1

print "ANSWER 2: %s" % answer_2_count

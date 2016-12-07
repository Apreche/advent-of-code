#!/usr/bin/env python
import collections

columns = ['' for i in range(9)]
with open('input.txt', 'r') as input_file:
    for line in input_file:
        for index, char in enumerate(line):
            columns[index] += char
columns = columns[:-1]

answer_one = ''
for column in columns:
    answer_one += collections.Counter(column).most_common(1)[0][0]

print "ANSWER 1: %s" % answer_one

answer_two = ''
for column in columns:
    answer_two += collections.Counter(column).most_common()[-1][0]

print "ANSWER 2: %s" % answer_two

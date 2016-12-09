#!/usr/bin/env python
import re

marker_pattern = re.compile(r'[\(](\d+)x(\d+)[\)]')

compressed = ''
remaining = ''
decompressed = ''
with open('input.txt', 'r') as input_file:
    remaining = compressed = input_file.read().strip()

# iterative partial decompression
index = 0
while remaining:
    match = marker_pattern.search(remaining)
    decompressed += remaining[0:match.start()]
    length, repeat = match.groups()
    length = int(length)
    repeat = int(repeat)
    tag_end = match.end()
    segment_end = tag_end + length
    repeat_segment = remaining[tag_end:segment_end]
    repeat_segment *= repeat
    decompressed += repeat_segment
    remaining = remaining[segment_end:]

print "ANSWER 1: %s" % len(decompressed.strip())

#!/usr/bin/env python
import re
import ipdb  # noqa

marker_pattern = re.compile(r'[\(](\d+)x(\d+)[\)]')

compressed = ''
remaining = ''
decompressed = ''
with open('input.txt', 'r') as input_file:
    remaining = compressed = input_file.read().strip()


# iterative partial decompression
while remaining:
    match = marker_pattern.search(remaining)
    if match is not None:
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
    else:
        decompressed += remaining
        remaining = ''

print "ANSWER 1: %s" % len(decompressed.strip())


# full recursive decompression count only
def full_decompress(compressed):
    decompressed_length = 0
    remaining = compressed
    while remaining:
        match = marker_pattern.search(remaining)
        if match is None:
            decompressed_length += len(remaining)
            remaining = ''
        else:
            decompressed_length += len(remaining[0:match.start()])
            length, repeat = match.groups()
            length = int(length)
            repeat = int(repeat)
            tag_end = match.end()
            segment_end = tag_end + length
            repeat_segment = remaining[tag_end:segment_end]
            decompressed_length += full_decompress(repeat_segment) * repeat
            remaining = remaining[segment_end:]
    return decompressed_length

print "ANSWER 2: %s" % full_decompress(compressed)

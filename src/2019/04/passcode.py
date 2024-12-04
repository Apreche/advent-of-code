#!/usr/bin/env python
import re
pattern = re.compile(r"(\d)\1+")

def has_repeat_digits(number):
    repeat_digits = [str(x) + str(x) for x in range(10)]
    return any(x in number for x in repeat_digits)

def has_repeat_digits_v2(number):
    match_lengths = []
    for match in pattern.finditer(number):
        match_lengths.append(len(match.group(0)))
    return 2 in match_lengths

def digits_always_increase(number):
    for x in range(0, len(number) - 1):
        pair = number[x:x+2]
        a = int(pair[0])
        b = int(pair[1])
        if b < a:
            return False
    return True

def check_range(low, high):
    valids = []
    for number in range(low, high+1):
        strnumber = str(number)
        if has_repeat_digits_v2(strnumber) and digits_always_increase(strnumber):
            valids.append(strnumber)
    return valids

if __name__ == "__main__":
    valids = check_range(231832, 767346)
    print(valids)
    print(len(valids))

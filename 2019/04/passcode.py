#!/usr/bin/env python

def has_repeat_digits(number):
    repeat_digits = [str(x) + str(x) for x in range(10)]
    return any(x in number for x in repeat_digits)

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
        if has_repeat_digits(strnumber) and digits_always_increase(strnumber):
            valids.append(strnumber)
    return valids

if __name__ == "__main__":
    valids = check_range(231832, 767346)
    print(len(valids))

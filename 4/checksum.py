#!/usr/bin/env python
import re

pattern = re.compile(r'([a-z\-]+)(\d+)\[([a-z]+)\]')

rooms = []
with open('input.txt', 'r') as input_file:
    for line in input_file:
        match = pattern.search(line)
        name, sector, checksum = match.groups()
        rooms.append([name, int(sector), checksum])


def advent_checksum(name):
    name = name.replace('-', '')
    letter_counts = {}
    for letter in name:
        letter_counts[letter] = name.count(letter)
    letter_counts = sorted(letter_counts.items(),
                           key=lambda x: (-x[1], x[0]))
    return ''.join([x[0] for x in letter_counts[:5]])


def decrypt_char(char, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char == '-':
        return ' '
    else:
        index = alphabet.index(char)
        new_index = (index + shift) % 26
        return alphabet[new_index]


def decrypt_name(encrypted_name, shift):
    decrypted_name = ''
    for char in encrypted_name:
        decrypted_name += decrypt_char(char, shift)
    return decrypted_name


sector_total = 0
for room in rooms:
    name, sector, checksum = room
    if advent_checksum(name) == checksum:
        sector_total += sector
        print "REAL: %s - %s" % (decrypt_name(name, sector), sector)

print ""
print "ANSWER 1: %s" % sector_total

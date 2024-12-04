#!/usr/bin/env python
import hashlib
import fish

door_id = 'abbhdwsy'


def md5hash(string):
    hasher = hashlib.md5()
    hasher.update(string)
    return hasher.hexdigest()

index = 0
password = ''
while len(password) < 8:
    string = "%s%s" % (door_id, index)
    checksum = md5hash(string)
    if checksum[:5] == '00000':
        password += checksum[5]
    index += 1
    fish.animate()

print "\n\nANSWER 1: %s\n\n" % password

password_two = ['' for x in range(8)]

index = 0
while '' in password_two:
    string = "%s%s" % (door_id, index)
    checksum = md5hash(string)
    if checksum[:5] == '00000':
        if checksum[5].isdigit():
            password_index = int(checksum[5])
            if password_index >= 0 and password_index < 8:
                password_char = checksum[6]
                if password_two[password_index] == '':
                    password_two[password_index] = password_char
    index += 1
    fish.animate()

print "\n\nANSWER 2: %s\n\n" % ''.join(password_two)

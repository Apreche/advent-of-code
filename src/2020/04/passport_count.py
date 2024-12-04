#!/usr/bin/env python

import re

REQUIRED_FIELDS = {
    'byr': r'^(19[2-8][0-9]|199[0-9]|200[0-2])$',
    'iyr': r'^(201[0-9]|2020)$',
    'eyr': r'^(202[0-9]|2030)$',
    'hgt': r'^(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))$',
    'hcl': r'^#[0-9a-f]{6}$',
    'ecl': r'^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid': r'^[0-9]{9}$',
}

OPTIONAL_FIELDS = [
    'cid',
]


def parse_input_file(filename: str):
    passports = []
    with open(filename) as input_file:
        current_passport = {}
        for line in input_file.read().splitlines():
            if len(line) == 0:
                passports.append(current_passport)
                current_passport = {}
            else:
                fields = line.split(' ')
                for field in fields:
                    pair = field.split(':')
                    current_passport[pair[0]] = pair[1]
        passports.append(current_passport)
    return passports


def validate_passport(passport):
    return all(
        [field in passport for field in REQUIRED_FIELDS]
    )


def fully_validate_passport(passport):
    validation = []
    for field_name, regex in REQUIRED_FIELDS.items():
        field_present = field_name in passport
        if field_present:
            field_valid = bool(
                re.search(
                    regex,
                    passport[field_name]
                )
            )
            validation.append(field_valid)
        else:
            validation.append(False)
    return all(validation)


def count_valid_passports(passports, validator=validate_passport):
    count = 0
    for passport in passports:
        if validator(passport):
            count += 1
    return count


if __name__ == "__main__":
    passport_data = parse_input_file('input.txt')
    result_one = count_valid_passports(
        passport_data,
        validator=validate_passport,
    )
    print(f"Part 1: {result_one}")
    result_two = count_valid_passports(
        passport_data,
        validator=fully_validate_passport,
    )
    print(f"Part 2: {result_two}")

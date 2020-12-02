#!/usr/bin/env python

def parse_input_line(line: str):
    quantity, char, value = tuple(line.split(' '))
    char = char[0:-1]
    qmin, qmax = tuple(quantity.split('-'))
    return {
        'min': int(qmin),
        'max': int(qmax),
        'char': char,
        'value': value
    }


def parse_input_file(filename: str):
    parsed_lines = []
    with open(filename) as input_file:
        parsed_lines = [parse_input_line(li) for li in input_file.read().splitlines()]
    return parsed_lines


def validate_password(parsed_line):
    count = parsed_line['value'].count(parsed_line['char'])
    return parsed_line['min'] <= count <= parsed_line['max']


if __name__ == '__main__':
    values = parse_input_file('input.txt')
    valid_passwords = [validate_password(pl) for pl in values]
    count_valid_passwords = valid_passwords.count(True)
    print(count_valid_passwords)

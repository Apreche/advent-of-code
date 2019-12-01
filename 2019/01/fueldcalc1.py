#!/usr/bin/env python

def fuelcalc(mass):
    return int(mass / 3) - 2

with open('input.txt', 'r') as input_file:
    module_masses = input_file.read().splitlines()

module_masses = [int(x) for x in module_masses]
fuel_needed = sum([fuelcalc(x) for x in module_masses])
print(fuel_needed)

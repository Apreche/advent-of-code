#!/usr/bin/env python

def fuelcalc(mass):
    fuel_mass = int(mass / 3) - 2
    if fuel_mass > 0:
        return fuel_mass + fuelcalc(fuel_mass)
    else:
        return 0

with open('input.txt', 'r') as input_file:
    module_masses = input_file.read().splitlines()

module_masses = [int(x) for x in module_masses]
fuel_needed = sum([fuelcalc(x) for x in module_masses])
print(fuel_needed)

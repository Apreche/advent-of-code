#!/usr/bin/env python

import re


def parse_input_file(filename: str):

    pattern = r'^(([a-z]+ )+)(\(contains ([a-z, ]+)\))$'

    with open(filename) as input_file:

        parsed_input = {}
        for food_id, line in enumerate(
            input_file.read().splitlines()
        ):
            match = re.search(
                pattern, line)
            ingredients = match.group(1)[0:-1].split(' ')
            allergens = tuple(
                match.group(4).split(', ')
            )
            parsed_input[food_id] = {
                'allergens': allergens,
                'ingredients': ingredients,
            }
    return parsed_input


def identify_possible_allergens(parsed_input):
    allergens = {}
    for food_id, food in parsed_input.items():
        for allergen in food['allergens']:
            allergens[allergen] = []

    for allergen in allergens:
        ingredient_counts = {}
        num_foods = 0
        for food in parsed_input.values():
            allergen_list = food['allergens']
            ingredient_list = food['ingredients']
            if allergen in allergen_list:
                num_foods += 1
                for ingredient in ingredient_list:
                    ingredient_counts.setdefault(
                        ingredient, 0
                    )
                    ingredient_counts[ingredient] += 1

        for ingredient, count in ingredient_counts.items():
            if count == num_foods:
                allergens[allergen].append(ingredient)
    return allergens


def count_good_ingredients(
    parsed_input,
    allergic_ingredients
):
    count = 0
    for food in parsed_input.values():
        ingredient_list = food['ingredients']
        for ingredient in ingredient_list:
            if ingredient not in allergic_ingredients:
                count += 1
    return count


def main():
    parsed_input = parse_input_file("input.txt")
    possible_allergens = identify_possible_allergens(
        parsed_input
    )

    allergic_ingredients = []
    for allergen, ingredients in possible_allergens.items():
        allergic_ingredients += ingredients
    allergic_ingredients = list(set(allergic_ingredients))

    part_1_result = count_good_ingredients(
        parsed_input, allergic_ingredients
    )
    print(f"Part 1: {part_1_result}\n")

    part_2_result = possible_allergens
    print("Part 2: Do by hand using the following data:\n")
    print(part_2_result)


if __name__ == "__main__":
    main()

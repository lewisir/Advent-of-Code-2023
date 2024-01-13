"""
--- Advent of Code 2023 ---
--- Day 8: Haunted Wasteland ---
https://adventofcode.com/2023/day/8
"""

import math
from time import perf_counter
import pprint

TEST = False

DAY = "8"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT


def get_input_data(filename):
    """function to read in the input data"""
    file_data = []
    with open(filename) as file:
        for line in file:
            file_data.append(line.rstrip("\n"))
    return file_data


def check_locations(locations):
    """for each loction check whether the destination has been reached and return true if all the locations have reached their destination"""
    for location in locations:
        if location[-1] != "Z":
            return False
    return True


def test_equality(item_list):
    """given a list of items return true if they are all equal to one another"""
    for item in item_list:
        if item_list.count(item) != len(item_list):
            return False
    return True


def find_lowest_position(number_list):
    """return the position of the lowest item in the list"""
    lowest_value = math.inf
    result_position = 0
    for position, number in enumerate(number_list):
        if number < lowest_value:
            lowest_value = number
            result_position = position
    return result_position


def gcf(a, b):
    """Return the Greatest Common Factor of the two integers a and b"""
    if b == 0:
        return a
    else:
        return gcf(b, a % b)


def lcm(a, b):
    """Return the Lowest Common Multiple of the two integers a and b"""
    return a * b // gcf(a, b)


def lowest_multiple(integers):
    """Return the lowest common multiple for the set of integers"""
    lowest = 1
    for integer in integers:
        lowest = lcm(lowest, integer)
    return lowest


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    network = {}
    for index, line in enumerate(data):
        if index > 1:
            node, elements = line.split(" = ")
            element1 = elements[1:4]
            element2 = elements[6:9]
            network[node] = (element1, element2)
        elif index == 0:
            instructions = line
    location = "AAA"
    i, steps = 0, 0
    while location != "ZZZ":
        direction = instructions[i]
        if direction == "R":
            index = 1
        elif direction == "L":
            index = 0
        location = network[location][index]
        steps += 1
        i += 1
        if i == len(instructions):
            i = 0
    print(f"Part I steps = {steps}")

    # Part two
    locations = []
    i, steps = 0, 0
    for node in network:
        if node[-1] == "A":
            locations.append(node)

    result_steps = []
    for location in locations:
        while location[-1] != "Z":
            direction = instructions[i]
            if direction == "R":
                index = 1
            elif direction == "L":
                index = 0
            location = network[location][index]
            steps += 1
            i += 1
            if i == len(instructions):
                i = 0
        result_steps.append(steps)
        i, steps = 0, 0

    print(f"Part II steps = {lowest_multiple(result_steps)}")


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

"""
--- Advent of Code 2023 ---
--- Day 14: Parabolic Reflector Dish ---
https://adventofcode.com/2023/day/14
"""

from time import perf_counter
from pprint import pprint

TEST = True

DAY = "14"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    platform = rotate(data)
    platform = tilt(platform)
    print(f"Part I Load = {total_load(platform)}")

    # Not figured an efficient way to do Part II yet
    platform = data
    load_list = []
    for _ in range(2000):
        platform = cycle(platform)
        load_list.append(total_load(platform))
    print(load_list[-30:])


def cycle(platform, number=1):
    """tilt the platform through all four directions the given number of times"""
    for _ in range(number * 4):
        platform = rotate(platform)
        platform = tilt(platform)
    return platform


def tilt(platform):
    """tilt the platform and return the new platform"""
    for i, line in enumerate(platform):
        platform[i] = roll_across_line(line)
    return platform


def total_load(platform):
    """calculate the total load on the platform"""
    load = 0
    for line in platform:
        load += line_weight(line)
    return load


def line_weight(line):
    """calculate the weight of a single line"""
    weight = 0
    for i, s in enumerate(line):
        if s == "O":
            weight += i + 1
    return weight


def rotate(matrix):
    """Given a 2 dimensional matrix, return a new 90 degree rotated matrix"""
    return ["".join(list(x)) for x in zip(*matrix[::-1])]


def roll_across_line(line):
    """Given a row or fixed rocks '#' and rolling rocks 'O', roll all the rocks across to the right"""
    sub_strings = line.split("#")
    for i, s in enumerate(sub_strings):
        sub_strings[i] = right_justify(s)
    return "#".join(sub_strings)


def right_justify(line):
    """move all the 'O' to the right hand side of the input line"""
    num_rocks = line.count("O")
    return "." * (len(line) - num_rocks) + "O" * num_rocks


def get_input_data(filename):
    """function to read in the input data"""
    file_data = []
    with open(filename) as file:
        for line in file:
            file_data.append(line.rstrip("\n"))
    return file_data


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

"""
--- Advent of Code 2023 ---
--- Day 14: Parabolic Reflector Dish ---
https://adventofcode.com/2023/day/14
"""

from time import perf_counter
from pprint import pprint

TEST = False

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
    # figure out the weight after each cycle and store in a list
    platform = data
    weight_list = []
    platform = rotate(platform)
    for _ in range(1000):
        platform = cycle(platform)
        weight_list.append(total_load(platform))
    search_result = search_pattern(weight_list)
    print(search_result)
    print(
        f"Part II - {calculate_value(1000000000,search_result[0]+1,search_result[1])}"
    )


def calculate_value(index, offset, pattern):
    """return the value at the index if the pattern were repeated after the offset"""
    return pattern[(index - offset) % len(pattern)]


def search_pattern(number_list):
    """Search the number_list for a repeating pattern. Pattern length must be at least 3 and must repeat at least 3 times
    The offset may be up to 1/4 of the length of the number_list
    Return the offset and the repeating pattern if found. Otherwise return False"""
    for offset in range(len(number_list) // 4):
        for pattern_length in range(2, ((len(number_list) - offset) // 3) + 1):
            if check_sub_list(
                number_list[offset:], number_list[offset : offset + pattern_length]
            ):
                return (offset, number_list[offset : offset + pattern_length])
    return False


def check_sub_list(main_list, sub_list):
    """Return true if the main list is a multiple of the sub list"""
    if sub_list * (len(main_list) // len(sub_list)) == main_list:
        return True
    else:
        return False


def cycle(platform):
    """tilt the platform through all four directions"""
    for i in range(4):
        platform = tilt(platform)
        platform = rotate(platform)
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

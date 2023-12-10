"""
--- Advent of Code 2023 ---
--- Day 9: Mirage Maintenance ---
https://adventofcode.com/2023/day/9
"""

import math
from time import perf_counter
import pprint

TEST = False

DAY = "9"
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


def sequence_diffs(number_list):
    """given a list of numbers, return a list of the differences between those numbers"""
    diff_list = []
    for position, number in enumerate(number_list):
        if position == len(number_list) - 1:
            pass
        else:
            diff_list.append(number_list[position + 1] - number_list[position])
    return diff_list


def next_number(number_list):
    """from the number list return the next number in the sequence"""
    diffs = sequence_diffs(number_list)
    if diffs.count(0) == len(number_list) - 1:
        return number_list[-1]
    else:
        return number_list[-1] + next_number(diffs)


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    extrapolated_sum = 0
    sequence_inputs = []
    for line in data:
        sequence = [int(x) for x in line.split()]
        sequence_inputs.append(sequence)
        extrapolated_sum += next_number(sequence)

    print(f"Part I - Extrapolated Sum = {extrapolated_sum}")


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

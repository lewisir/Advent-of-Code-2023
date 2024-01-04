"""
--- Advent of Code 2023 ---
--- Day 16: _______________ ---
https://adventofcode.com/2023/day/16
"""

from time import perf_counter
from pprint import pprint

TEST = True

DAY = "16"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT

DIRECTIONS = ["U", "D", "L", "R"]
COORDINATES = ["y", "x"]


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    pprint(data)


def process_data(data):
    """Convert the strings in to lists"""
    output = []
    for line in data:
        output.append([x for x in line])
    return output


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

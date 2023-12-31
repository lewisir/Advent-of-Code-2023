"""
--- Advent of Code 2023 ---
--- Day 15: Lens Library ---
https://adventofcode.com/2023/day/15
"""

from time import perf_counter
from pprint import pprint

TEST = False

DAY = "15"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    initialization_sequence = data[0].split(',')
    hash_sum = 0
    for step in initialization_sequence:
        hash_sum += hash(step)

    print(f"Part I Hash Sum is {hash_sum}")


def hash(input_string):
    """Return the hash value of the input string"""
    value = 0
    for s in input_string:
        value += ord(s)
        value *= 17
        value = value%256
    return value



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

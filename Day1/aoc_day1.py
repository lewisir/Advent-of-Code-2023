"""
--- Advent of Code 2023 ---
--- Day 18:  ---
https://adventofcode.com/2023/day/1
"""

from time import perf_counter

TEST = False

DAY = "1"
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


def main():
    """Main program"""
    data = get_input_data(FILENAME)


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

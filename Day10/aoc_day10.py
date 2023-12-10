"""
--- Advent of Code 2023 ---
--- Day 10: Pipe Maze ---
https://adventofcode.com/2023/day/10
"""

import math
from time import perf_counter
import pprint

TEST = False

DAY = "10"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT

DIRECTIONS = ["N", "S", "E", "W"]
VALID_MOVES = {
    "N": ("|", "7", "F"),
    "S": ("|", "L", "J"),
    "E": ("-", "7", "J"),
    "W": ("-", "L", "F"),
}

PIPES = {
    "|": {"N": ("N", -1, 0), "S": ("S", +1, 0)},
    "-": {"E": ("E", 0, +1), "W": ("W", 0, -1)},
    "L": {"S": ("E", 0, +1), "W": ("N", -1, 0)},
    "J": {"S": ("W", 0, -1), "E": ("N", -1, 0)},
    "7": {"N": ("W", 0, -1), "E": ("S", +1, 0)},
    "F": {"N": ("E", 0, +1), "W": ("S", +1, 0)},
}


def get_input_data(filename):
    """function to read in the input data"""
    file_data = []
    with open(filename) as file:
        for line in file:
            file_data.append(line.rstrip("\n"))
    return file_data


def find_start(pipe_map, start="S"):
    """return the position in the pipe_map of the starting position (y,x)"""
    for y in range(len(pipe_map)):
        for x in range(len(pipe_map[0])):
            if pipe_map[y][x] == start:
                return (y, x)


def find_valid_move(pipe_map, start_position):
    """Given the starting position find a valid fist move retruning the dirction taken and the next position"""
    y, x = start_position
    for direction in DIRECTIONS:
        if direction == "N" and y != 0:
            new_y, new_x = y - 1, x
        elif direction == "S" and y != len(pipe_map) - 1:
            new_y, new_x = y + 1, x
        elif direction == "E" and x != len(pipe_map[0]) - 1:
            new_y, new_x = y, x + 1
        elif direction == "W" and x != 0:
            new_y, new_x = y, x - 1
        if pipe_map[new_y][new_x] in VALID_MOVES[direction]:
            return direction, new_y, new_x
    return False


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    start_position = find_start(data)
    move_count = 0
    direction, y, x = find_valid_move(data, start_position)
    symbol = data[y][x]
    while symbol is not "S":
        direction, change_y, change_x = PIPES[symbol][direction]
        y += change_y
        x += change_x
        symbol = data[y][x]
        move_count += 1
    print(f"Part 1 {(move_count+1)/2}")


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

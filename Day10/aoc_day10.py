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

ADJ_POINTS = {
    "N": {"LHS": (0, -1), "RHS": (0, +1)},
    "S": {"LHS": (0, +1), "RHS": (0, -1)},
    "E": {"LHS": (-1, 0), "RHS": (+1, 0)},
    "W": {"LHS": (+1, 0), "RHS": (-1, 0)},
}

TURNS = {
    "N": {"N": 0, "W": -1, "E": +1},
    "S": {"S": 0, "W": +1, "E": -1},
    "E": {"E": 0, "N": -1, "S": +1},
    "W": {"W": 0, "N": +1, "S": -1},
}


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    start_position = find_start(data)
    move_count = 0
    direction, y, x = find_valid_move(data, start_position)
    symbol = data[y][x]
    pipe_path = set(())
    pipe_path.add((y, x))
    left_points = set(())
    right_points = set(())
    right_turns = 0
    while symbol != "S":
        lhs = ADJ_POINTS[direction]["LHS"]
        rhs = ADJ_POINTS[direction]["RHS"]
        if test_within_map(data, (y + lhs[0], x + lhs[1])):
            left_points.add((y + lhs[0], x + lhs[1]))
        if test_within_map(data, (y + rhs[0], x + rhs[1])):
            right_points.add((y + rhs[0], x + rhs[1]))
        old_direction = direction
        direction, change_y, change_x = PIPES[symbol][direction]
        y += change_y
        x += change_x
        pipe_path.add((y, x))
        right_turns += TURNS[old_direction][direction]
        symbol = data[y][x]
        move_count += 1

    print(f"Part 1 {(move_count+1)/2}")
    left_points.difference_update(pipe_path)
    right_points.difference_update(pipe_path)

    inside_points = set(())
    if right_turns > 0:
        start_points = right_points
        alt_start_pts = left_points
    else:
        start_points = left_points
        alt_start_pts = right_points
    for point in start_points:
        inside_points = inside_points.union(map_out_points(data, pipe_path, point))

    print(f"Part II Inside tiles = {len(inside_points)}")
    # first run answer 397 is too low

    # second answer of 408 is too high (calculated by using the outside points below)
    # outside_points = set(())
    # for point in alt_start_pts:
    #    outside_points = outside_points.union(map_out_points(data, pipe_path, point))
    # print(f"Total Points = {len(data)*len(data[0])}")
    # print(f"Pipe Points = {len(pipe_path)}")
    # print(f"Outside Points = {len(outside_points)}")
    # print(
    #    f"Alt calc of inside points = {len(data)*len(data[0])-len(pipe_path)-len(outside_points)}"
    # )


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
    if y != 0 and pipe_map[y - 1][x] in VALID_MOVES["N"]:
        return ("N", y - 1, x)
    elif y != len(pipe_map) - 1 and pipe_map[y + 1][x] in VALID_MOVES["S"]:
        return ("S", y + 1, x)
    elif x != 0 and pipe_map[y][x - 1] in VALID_MOVES["W"]:
        return ("W", y, x - 1)
    elif x != len(pipe_map[0]) - 1 and pipe_map[y][x + 1] in VALID_MOVES["E"]:
        return ("E", y, x + 1)
    return False


def test_within_map(map, location):
    """Return True of the location is within the map"""
    y, x = location
    if y >= 0 and y < (len(map)) and x >= 0 and x < len(map[0]):
        return True
    else:
        return False


def map_out_points(map, boundary, point):
    """Return the set of points from the map that are adjacent to the input set of points and are bounded by the boundary"""
    output_points = set(())
    output_points.add(point)
    next_points = [point]
    while len(next_points) > 0:
        current_point = next_points.pop(0)
        adjacent_points = find_adjacent_points(map, current_point)
        adjacent_points.difference_update(boundary)
        for adjacency in adjacent_points:
            if adjacency not in output_points:
                output_points.add(adjacency)
                next_points.append(adjacency)
    return output_points


def find_adjacent_points(map, point):
    """Return the set of points adjacent to the point in the map"""
    output_points = set(())
    y, x = point
    if test_within_map(map, (y - 1, x)):
        output_points.add((y - 1, x))
    if test_within_map(map, (y + 1, x)):
        output_points.add((y + 1, x))
    if test_within_map(map, (y, x - 1)):
        output_points.add((y, x - 1))
    if test_within_map(map, (y, x + 1)):
        output_points.add((y, x + 1))
    return output_points


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

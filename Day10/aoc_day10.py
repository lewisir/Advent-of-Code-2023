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

TURN_FWD_ADJ_POINTS = {
    "N": (-1, 0),
    "S": (+1, 0),
    "E": (0, +1),
    "W": (0, -1),
}


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    start_position = find_start(data)
    pipe_points, inside_adj_points = trace_pipe(data, start_position)
    print(f"Part I - Pipe's furthest point {len(pipe_points)//2}")

    inside_points = set(())
    for point in inside_adj_points:
        inside_points = inside_points.union(map_out_points(data, pipe_points, point))
    print(f"Part II - Tiles within the pipe {len(inside_points)}")
    # Part II 397 is too low and 408 is too high
    # even after adding the extra turn points !!! So where is it going wrong? Unless I have it wrong...
    # My test proves the extra TURN_FWD_ADJ_POINTS does work, but this does not change my result for my real data


def trace_pipe(pipe_map, start):
    """From the start position in the pipe map, trace the path of the pipe retrning the points of the pipe and the inside adjacent points"""
    pipe_points = set(())
    lhs_points = set(())
    rhs_points = set(())
    right_turn_count = 0
    direction, y, x = find_valid_move(pipe_map, start)
    original_direction = direction
    symbol = pipe_map[y][x]
    while symbol != "S":
        pipe_points.add((y, x))
        lhs = ADJ_POINTS[direction]["LHS"]
        rhs = ADJ_POINTS[direction]["RHS"]
        lhs_points.add((y + lhs[0], x + lhs[1]))
        rhs_points.add((y + rhs[0], x + rhs[1]))
        previous_direction = direction
        direction, change_y, change_x = PIPES[symbol][direction]
        right_turn_count += TURNS[previous_direction][direction]
        if TURNS[previous_direction][direction] > 0:
            lhs_points.add(
                (
                    y + TURN_FWD_ADJ_POINTS[direction][0],
                    x + TURN_FWD_ADJ_POINTS[direction][1],
                )
            )
        elif TURNS[previous_direction][direction] < 0:
            rhs_points.add(
                (
                    y + TURN_FWD_ADJ_POINTS[direction][0],
                    x + TURN_FWD_ADJ_POINTS[direction][1],
                )
            )
        y += change_y
        x += change_x
        symbol = pipe_map[y][x]
    # add in the starting position to the pipe points
    pipe_points.add((y, x))
    lhs = ADJ_POINTS[direction]["LHS"]
    rhs = ADJ_POINTS[direction]["RHS"]
    lhs_points.add((y + lhs[0], x + lhs[1]))
    rhs_points.add((y + rhs[0], x + rhs[1]))
    if TURNS[original_direction][direction] > 0:
        lhs_points.add(
            (
                y + TURN_FWD_ADJ_POINTS[direction][0],
                x + TURN_FWD_ADJ_POINTS[direction][1],
            )
        )
    elif TURNS[original_direction][direction] < 0:
        rhs_points.add(
            (
                y + TURN_FWD_ADJ_POINTS[direction][0],
                x + TURN_FWD_ADJ_POINTS[direction][1],
            )
        )
    if right_turn_count > 0:
        inside_adj_points = rhs_points
    else:
        inside_adj_points = lhs_points
    inside_adj_points.difference_update(pipe_points)
    inside_adj_points = remove_out_of_boundary(pipe_map, inside_adj_points)
    return pipe_points, inside_adj_points


def remove_out_of_boundary(pipe_map, points):
    """From the set of points remove any tht lie outside the pipe_map boundary"""
    exterior_points = set(())
    for point in points:
        y, x = point
        if y < 0 or y >= len(pipe_map) or x < 0 or x >= len(pipe_map[0]):
            exterior_points.add((y, x))
    resulting_points = points.difference(exterior_points)
    return resulting_points


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

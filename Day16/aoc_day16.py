"""
--- Advent of Code 2023 ---
--- Day 16: The Floor Will Be Lava ---
https://adventofcode.com/2023/day/16
"""

from time import perf_counter
from pprint import pprint

TEST = False

DAY = "16"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT

COORDINATES = {"U": (-1, 0), "D": (+1, 0), "L": (0, -1), "R": (0, +1)}
BEAM_REFRACTOR = {
    "U": {
        ".": ("U"),
        "/": ("R"),
        "\\": ("L"),
        "|": ("U"),
        "-": ("L", "R"),
    },
    "D": {
        ".": ("D"),
        "/": ("L"),
        "\\": ("R"),
        "|": ("D"),
        "-": ("L", "R"),
    },
    "L": {
        ".": ("L"),
        "/": ("D"),
        "\\": ("U"),
        "|": ("D", "U"),
        "-": ("L"),
    },
    "R": {
        ".": ("R"),
        "/": ("U"),
        "\\": ("D"),
        "|": ("D", "U"),
        "-": ("R"),
    },
}


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    energized_tiles = beam_trace(data, "R", (0, 0), set(()))
    print(
        f"Part 1 - number of energized tiles = {len(filter_beam_path(energized_tiles))}"
    )
    max_energized_tiles = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if y == 0:
                direction = "D"
            elif y == len(data) - 1:
                direction = "U"
            if x == 0:
                direction = "R"
            elif x == len(data[0]) - 1:
                direction = "L"
            # But need to also run extra beams in the corners (see below the extra steps)
            energized_tiles = len(
                filter_beam_path(beam_trace(data, direction, (y, x), set(())))
            )
            if energized_tiles > max_energized_tiles:
                max_energized_tiles = energized_tiles
    energized_tiles = len(filter_beam_path(beam_trace(data, "D", (0, 0), set(()))))
    if energized_tiles > max_energized_tiles:
        max_energized_tiles = energized_tiles
    energized_tiles = len(
        filter_beam_path(beam_trace(data, "D", (0, len(data) - 1), set(())))
    )
    if energized_tiles > max_energized_tiles:
        max_energized_tiles = energized_tiles
    energized_tiles = len(filter_beam_path(beam_trace(data, "U", (0, 0), set(()))))
    if energized_tiles > max_energized_tiles:
        max_energized_tiles = energized_tiles
    energized_tiles = len(
        filter_beam_path(beam_trace(data, "U", (0, len(data) - 1), set(())))
    )
    if energized_tiles > max_energized_tiles:
        max_energized_tiles = energized_tiles
    print(f"Part II - Max Energized Tiles = {max_energized_tiles}")


def beam_trace(layout, direction, location, beam_path):
    """Given a location in the layout and a beam direction, trace the beam adding the points visited to the set and return that set"""
    beam_active = True
    while beam_active:
        if (direction, location) not in beam_path:
            beam_path.add((direction, location))
            y, x = location
            optic_element = layout[y][x]
            if len(BEAM_REFRACTOR[direction][optic_element]) > 1:
                split_direction = BEAM_REFRACTOR[direction][optic_element][1]
                sy, sx = COORDINATES[split_direction]
                split_location = (y + sy, x + sx)
                if layout_edge(layout, split_location):
                    beam_path.update(
                        beam_trace(layout, split_direction, split_location, beam_path)
                    )
            direction = BEAM_REFRACTOR[direction][optic_element][0]
            dy, dx = COORDINATES[direction]
            location = (y + dy, x + dx)
            beam_active = layout_edge(layout, location)
        else:
            beam_active = False
    return beam_path


def layout_edge(layout, location):
    """Return False if the location is outside the bounds of the layout"""
    y, x = location
    if y < 0 or y >= len(layout):
        return False
    elif x < 0 or x >= len(layout[0]):
        return False
    else:
        return True


def filter_beam_path(beam_path):
    """Filter the set of direction,location tuples to contain unique locations"""
    ouput_set = set(())
    for item in beam_path:
        ouput_set.add(item[1])
    return ouput_set


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

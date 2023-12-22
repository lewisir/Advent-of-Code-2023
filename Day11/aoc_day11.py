"""
--- Advent of Code 2023 ---
--- Day 11: Cosmic Expansion ---
https://adventofcode.com/2023/day/11
"""

from time import perf_counter

TEST = False

DAY = "11"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    galaxies = find_galaxies(data)
    empty_rows = find_empty_rows(galaxies)
    empty_cols = find_empty_cols(galaxies)
    expand_rows(galaxies, empty_rows)
    expand_cols(galaxies, empty_cols)
    print(f"Part 1 - {sum(distances(galaxies))}")

    # Part II
    galaxies = find_galaxies(data)
    empty_rows = find_empty_rows(galaxies)
    empty_cols = find_empty_cols(galaxies)
    expand_rows(galaxies, empty_rows, 999999)
    expand_cols(galaxies, empty_cols, 999999)
    print(f"Part 2 - {sum(distances(galaxies))}")


def expand_rows(galaxies, empty_rows, expansion_factor=1):
    """given the galaxy positions and the empty rows, change the galaxy's positions by expanding the empty rows"""
    for galaxy in galaxies:
        galaxy[0] = (
            galaxy[0] + count_less_than(empty_rows, galaxy[0]) * expansion_factor
        )
    return galaxies


def expand_cols(galaxies, empty_cols, expansion_factor=1):
    """given the galaxy positions and the empty cols, change the galaxy's positions by expanding the empty cols"""
    for galaxy in galaxies:
        galaxy[1] = (
            galaxy[1] + count_less_than(empty_cols, galaxy[1]) * expansion_factor
        )
    return galaxies


def count_less_than(collection, number):
    """return the number of items in the collection that are less than the number given"""
    count = 0
    for item in collection:
        if item < number:
            count += 1
    return count


def find_galaxies(image):
    """Search the image for the positions of the galaxies"""
    galaxies = []
    for row, line in enumerate(image):
        for column, pixel in enumerate(line):
            if pixel == "#":
                galaxies.append([row, column])
    return galaxies


def find_empty_rows(galaxies):
    """given the positions of the galaxies, return the rows that contain no galaxies"""
    rows_with_galaxies = set(())
    max_row = 0
    for galaxy in galaxies:
        if galaxy[0] > max_row:
            max_row = galaxy[0]
        rows_with_galaxies.add(galaxy[0])
    all_rows = set(range(0, max_row + 1))
    all_rows.difference_update(rows_with_galaxies)
    return all_rows


def find_empty_cols(galaxies):
    """given the positions of the galaxies, return the columns that contain no galaxies"""
    cols_with_galaxies = set(())
    max_col = 0
    for galaxy in galaxies:
        if galaxy[1] > max_col:
            max_col = galaxy[1]
        cols_with_galaxies.add(galaxy[1])
    all_cols = set(range(0, max_col + 1))
    all_cols.difference_update(cols_with_galaxies)
    return all_cols


def distances(galaxies):
    """Given a collection of positions, return the distances between each pair of positions"""
    galaxy_distances = []
    for number1, galaxy1 in enumerate(galaxies):
        for number2, galaxy2 in enumerate(galaxies):
            if number1 < number2:
                galaxy_distances.append(get_distance(galaxy1, galaxy2))
    return galaxy_distances


def get_distance(galaxy1, galaxy2):
    """return the distance between a pair of galaxies"""
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


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

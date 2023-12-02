"""
--- Advent of Code 2023 ---
--- Day 2: Cube Conundrum ---
https://adventofcode.com/2023/day/2
"""

from time import perf_counter

TEST = False

DAY = "2"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT

COLOUR_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


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

    game_total = 0
    for game in data:
        game_possible = True
        game_number = int(game.split(":")[0][5:])
        game_subsets = game.split(":")[1].split(";")
        for subset in game_subsets:
            cube_results = subset.split(",")
            for result in cube_results:
                number_of_cubes, colour_of_cubes = result.split()
                if int(number_of_cubes) > COLOUR_LIMITS[colour_of_cubes]:
                    game_possible = False
                    break
        if game_possible:
            game_total += game_number
    print(f"Part I - Game Total: {game_total}")

    game_total = 0
    for game in data:
        game_power = 1
        least_colours = {
            "red": 1,
            "green": 1,
            "blue": 1,
        }
        game_number = int(game.split(":")[0][5:])
        game_subsets = game.split(":")[1].split(";")
        for subset in game_subsets:
            cube_results = subset.split(",")
            for result in cube_results:
                number_of_cubes, colour_of_cubes = result.split()
                if int(number_of_cubes) > least_colours[colour_of_cubes]:
                    least_colours[colour_of_cubes] = int(number_of_cubes)
        for x in least_colours.values():
            game_power *= x
        game_total += game_power
    print(f"Part II - Game Total: {game_total}")


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

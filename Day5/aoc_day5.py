"""
--- Advent of Code 2023 ---
--- Day 5: If You Give A Seed A Fertilizer ---
https://adventofcode.com/2023/day/5
"""

from time import perf_counter
import pprint

TEST = False

DAY = "5"
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
    maps = []
    for line in data:
        if line != "":
            if line[:6] == "seeds:":
                seeds = line[7:].split()
                seeds = [int(x) for x in seeds]
            elif line[-1] == ":":
                maps.append([])
            else:
                destination_start, source_start, map_range = [
                    int(x) for x in line.split()
                ]
                maps[-1].append(
                    {
                        "source_start": source_start,
                        "destination_start": destination_start,
                        "map_range": map_range,
                    }
                )
    mapped_seeds = []
    for seed in seeds:
        mapped_number = seed
        # print(f"new seed :{seed}")
        for map in maps:
            # print("new-map")
            for number_map in map:
                if (
                    mapped_number >= number_map["source_start"]
                    and mapped_number
                    < number_map["source_start"] + number_map["map_range"]
                ):
                    mapped_number += (
                        number_map["destination_start"] - number_map["source_start"]
                    )
                    break
                # print(mapped_number)
        mapped_seeds.append(mapped_number)
    mapped_seeds.sort()
    print(mapped_seeds)


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

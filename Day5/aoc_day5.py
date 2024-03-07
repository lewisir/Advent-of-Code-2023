"""
--- Advent of Code 2023 ---
--- Day 5: If You Give A Seed A Fertilizer ---
https://adventofcode.com/2023/day/5
"""

from time import perf_counter
import pprint

TEST = True

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


def map_seed_number(seed, maps):
    mapped_number = seed
    # print(f"new seed :{seed}")
    for map in maps:
        # print("new-map")
        for number_map in map:
            if (
                mapped_number >= number_map["src_start"]
                and mapped_number < number_map["src_start"] + number_map["map_range"]
            ):
                mapped_number += number_map["dst_start"] - number_map["src_start"]
                break
            # print(mapped_number)
    return mapped_number


def split_range(input_info, map_info):
    """Return two lists. One containing the part(s) of the input range that are not changed
      and the other containing the part of the input rage that are changed
    Return empty lists if there is no transformation"""
    in_start, in_range = input_info
    in_end = in_start + in_range - 1
    map_end = map_info["src_start"] + map_info["map_range"] - 1
    if map_info["src_start"] <= in_start and map_end >= in_end:
        # The entire input is covered by the map
        out_start = map_info["dst_start"] + in_start - map_info["src_start"]
        out_range = in_range
        return [],[(out_start, out_range)]
    elif map_info["src_start"] <= in_start and map_end > in_start and map_end < in_end:
        # The begining of the input is mapped
        out_start = map_info["dst_start"] + in_start - map_info["src_start"]
        out_range = map_end - in_start + 1
        in_unmapped_start = map_end + 1
        in_unmapped_range = in_end - map_end
        return [(in_unmapped_start, in_unmapped_range)],[(out_start, out_range)]
    elif (
        map_info["src_start"] > in_start
        and map_info["src_start"] <= in_end
        and map_end > in_end
    ):
        # The end of the input is mapped
        out_start = map_info["dst_start"]
        out_range = in_end - map_info["src_start"] + 1
        in_unmapped_start = in_start
        in_unmapped_range = map_info["src_start"] - in_start
        return [(in_unmapped_start, in_unmapped_range)],[(out_start, out_range)]
    elif map_info["src_start"] > in_start and map_end < in_end:
        # A middle section of the input is mapped
        out_start = map_info["dst_start"]
        out_range = map_info["map_range"]
        in_unmapped1_start = in_start
        in_unmapped1_range = map_info["src_start"] - in_start
        in_unmapped2_start = map_end + 1
        in_unmapped2_range = map_end - in_start
        return [(in_unmapped1_start, in_unmapped1_range),(in_unmapped2_start, in_unmapped2_range)],[(out_start, out_range)]
    else:
        # None of the input is mapped
        return [(in_start, in_range)],[]

def process_seed_ranges(seed_ranges, map_info):
    """process the serires of seed ranges with the map info returning the unchanged and changed ranges"""
    original_ranges, updated_ranges =[],[]
    for seed_range in seed_ranges:
        unchanged_ranges, new_ranges = split_range(seed_range,map_info)
        original_ranges.extend(unchanged_ranges)
        updated_ranges.extend(new_ranges)
        print(f"seed range is {seed_range}\noriginal is now {original_ranges}\nupdated is now {updated_ranges}")
    return original_ranges,updated_ranges


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
                dst_start, src_start, map_range = [int(x) for x in line.split()]
                maps[-1].append(
                    {
                        "src_start": src_start,
                        "dst_start": dst_start,
                        "map_range": map_range,
                    }
                )
    mapped_seeds = []
    for seed in seeds:
        mapped_seeds.append(map_seed_number(seed, maps))
    mapped_seeds.sort()
    print(f"Part I lowset location number - {mapped_seeds[0]}")

    pprint.pprint(maps[0][0])

    seed_ranges = []
    for i in range(1, len(seeds), 2):
        seed_ranges.append((seeds[i - 1], seeds[i]))

    print(f"Seed Ranges - {seed_ranges}")

    pprint.pprint(process_seed_ranges(seed_ranges,maps[0][0]))
    


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

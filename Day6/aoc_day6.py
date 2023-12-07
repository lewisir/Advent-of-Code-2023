"""
--- Advent of Code 2023 ---
--- Day 6: Wait For It ---
https://adventofcode.com/2023/day/6
"""

from time import perf_counter
import pprint

TEST = False

DAY = "6"
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


def find_times(total_time, min_distance):
    """return the charge times that mean the distance travelled is greater than the provided distance"""
    successful_times = []
    for t in range(1, total_time):
        distance = t * (total_time - t)
        if distance > min_distance:
            successful_times.append(t)
    return len(successful_times)


def join_list_items(my_list):
    """given a list of text, return a string that is the contatenation of the list"""
    output = ""
    for item in my_list:
        if not isinstance(item, str):
            return False
        else:
            output += item
    return output


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    times = [int(x) for x in data[0].split()[1:]]
    distances = [int(x) for x in data[1].split()[1:]]
    races = iter(zip(times, distances))
    successes = 1
    print((races))
    for race in tuple(races):
        successes *= find_times(race[0], race[1])
    print(f"Part 1 - result = {successes}")

    times = data[0].split()[1:]
    distances = data[1].split()[1:]
    time = int(join_list_items(times))
    distance = int(join_list_items(distances))

    print(f"Part II - total = {find_times(time,distance)}")


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

"""
--- Advent of Code 2023 ---
--- Day 12: Hot Springs ---
https://adventofcode.com/2023/day/12
"""

from time import perf_counter

TEST = False

DAY = "12"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT

MULTIPLIER = 1


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    count = 0
    for line in data:
        spring_string, damaged_data = line.split(" ")
        damaged_data = damaged_data.split(",")
        damaged_data = tuple([int(x) for x in damaged_data])
        spring_string = grow_string(spring_string, MULTIPLIER)
        damaged_data = damaged_data * MULTIPLIER
        count += permute_string(spring_string, damaged_data)
    print(f"Count = {count}")

    # Odd, but if I pass in a list rather than a tuple I get a wrong answer in some cases - permute_string("????.#...#...", [4, 1, 1]) != 1 !!!


def permute_string(input_string, damaged_data, count=0):
    """Recursively calculate the number of permutation of the given string and damaged spring data"""
    if input_string.find("?") > -1:
        next_section = input_string[: input_string.find("?")]
        next_section_damaged_data = calculate_damaged_spring_data(next_section)
        if match_sequences(next_section_damaged_data, damaged_data):
            # The start of the input string is good so pass the remaining part of the string to permute_string
            remaining_string = input_string[input_string.find("?") + 1 :]
            remaining_damaged_data = subtract_sequences(
                damaged_data, next_section_damaged_data
            )
            count = permute_string(remaining_string, remaining_damaged_data, count)
        # check if there are enough '?' for the remaining '#' and if there are then pass the input_string with the first '?' replaced with '#' to permute_string
        if input_string.count("?") >= sum(damaged_data) - input_string.count("#"):
            next_string = (
                next_section + "#" + input_string[input_string.find("?") + 1 :]
            )
            count = permute_string(next_string, damaged_data, count)
    else:
        if calculate_damaged_spring_data(input_string) == damaged_data:
            count += 1
    return count


def calculate_damaged_spring_data(spring_string):
    """Return a tuple of the damaged spring data based on the spring_string"""
    count = 0
    damaged_spring_data = []
    for c in spring_string:
        if c == "#":
            count += 1
        elif c == "." and count > 0:
            damaged_spring_data.append(count)
            count = 0
    if count > 0:
        damaged_spring_data.append(count)
    return tuple(damaged_spring_data)


def match_sequences(sequence_1, sequence_2):
    """Return true if the start of the two lists are the same. Also return true if one list is empty"""
    for pair in zip(sequence_1, sequence_2):
        if pair[0] != pair[1]:
            return False
    return True


def subtract_sequences(sequence_1, sequence_2):
    """return a tuple of the remaining items in the longer sequence once the items from the short sequence have been removed"""
    if match_sequences(sequence_1, sequence_2):
        if len(sequence_1) < len(sequence_2):
            return tuple(sequence_2[len(sequence_1) :])
        else:
            return tuple(sequence_1[len(sequence_2) :])
    else:
        return None


def grow_string(input_string, n, separator="?"):
    """Return a string that is a repeat of the input_string  n times joined by the separator"""
    output_string = input_string
    for _ in range(n - 1):
        output_string += separator + input_string
    return output_string


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

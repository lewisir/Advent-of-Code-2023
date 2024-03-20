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


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    result_list = []
    for line in data:
        alternative = 0
        spring_data, damaged_springs = line.split(" ")
        damaged_springs = damaged_springs.split(",")
        damaged_springs = [int(x) for x in damaged_springs]
        total_damaged_springs = sum(damaged_springs)
        unknown_spring_locations = find_char_positions(spring_data, "?")
        known_damaged_springs = len(find_char_positions(spring_data, "#"))
        possible_damaged_springs = generate_combinations(
            unknown_spring_locations, total_damaged_springs - known_damaged_springs
        )
        for possible in possible_damaged_springs:
            test_data = create_spring_data(spring_data, possible)
            if get_damaged_springs(test_data) == damaged_springs:
                alternative += 1
        result_list.append(alternative)
    print(f"Part 1 - sum of alternatives = {sum(result_list)}")
    # Part I works but is slow (about 5 seconds)

    # New approach is to work through the string section by section (delimited by groups of '#') and check as we go whether we're producing a string that will match the damaged spring summary data 


def generate_combinations(arr, r):
    data = [0] * r
    return combination_util(arr, data, 0, len(arr) - 1, 0, r, combinations=[])


def combination_util(arr, data, start, end, index, r, combinations):
    """Grabbed this from Internet to produce all the combinations of length 'r' from the list 'arr'"""
    if index == r:
        combinations.append(data.copy())
        return combinations
    i = start
    while i <= end and end - i + 1 >= r - index:
        data[index] = arr[i]
        combination_util(arr, data, i + 1, end, index + 1, r, combinations)
        i += 1
    return combinations


def find_char_positions(input_string, char):
    """return a list of the positions in the string where the char appears"""
    output_list = []
    for i, c in enumerate(input_string):
        if c == char:
            output_list.append(i)
    return output_list


def get_damaged_springs(input_list):
    """given a input containing #'s separated by .'s, return a list containing the numbers of contiguous #'s"""
    hash_count = 0
    output_list = []
    for c in input_list:
        if c == "#":
            hash_count += 1
        elif c == "." and hash_count > 0:
            output_list.append(hash_count)
            hash_count = 0
    if hash_count > 0:
        output_list.append(hash_count)
    return output_list


def create_spring_data(input_string, positions):
    """Create an output string from the input string replacing '?' with either '.' or '#' as dictated by the positions"""
    output_string = ""
    for i, c in enumerate(input_string):
        if c == ".":
            output_string += "."
        elif c == "#":
            output_string += "#"
        elif c == "?" and i in positions:
            output_string += "#"
        else:
            output_string += "."
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

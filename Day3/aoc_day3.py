"""
--- Advent of Code 2023 ---
--- Day 3: Gear Ratios ---
https://adventofcode.com/2023/day/3
"""

from time import perf_counter

TEST = False

DAY = "3"
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


def find_numbers(string, row):
    """given a string, find the numbers and their positions in the string
    return a list of tuples, each tuple is a number found and the range of positions in the string that number is at
    """
    number_found = False
    new_number = ""
    result_list = []
    start, end = None, None
    for i, c in enumerate(string):
        if c.isdigit():
            if number_found is not True:
                start = i
            number_found = True
            new_number += c
        else:
            number_found = False
            end = i
            if start is not None:
                number_entry = (int(new_number), row, [start, end])
                result_list.append(number_entry)
                new_number = ""
                start, end = None, None
    # this IF block catches numbers that are at the end of a line
    if start is not None:
        number_entry = (int(new_number), row, [start, len(string) - 1])
        result_list.append(number_entry)
    return result_list


def adjacent_symbol(data, number_location):
    """Given the data and the location of the number, return whether there is an adjacent symbol
    The number location is the row in the data and the range (slice) the number is located at
    """
    row = number_location[1]
    number_location_start = number_location[2][0]
    number_location_end = number_location[2][1]
    if row == 0:
        row_start = 0
        row_end = row + 2
    elif row == len(data) - 1:
        row_start = row - 1
        row_end = len(data) - 1
    else:
        row_start = row - 1
        row_end = row + 2

    if number_location_start == 0:
        start = 0
        end = number_location_end + 1
    elif number_location_end == len(data[0]) - 1:
        start = number_location_start - 1
        end = number_location_end
    else:
        start = number_location_start - 1
        end = number_location_end + 1

    for row in range(row_start, row_end):
        for position in range(start, end):
            charcter = data[row][position]
            if not charcter.isdigit() and charcter != ".":
                return True
    return False


def find_multipliers(string, row):
    """given a string, find the '*'s and their positions in the string
    return a list of tuples, each tuple is the row and position of the '*'"""
    result_list = []
    for i, c in enumerate(string):
        if c == "*":
            result_entry = (row, i)
            result_list.append(result_entry)
    return result_list


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    number_locations = []
    multiplier_locations = []
    number_sum = 0
    for row, line in enumerate(data):
        numbers = find_numbers(line, row)
        if len(numbers) > 0:
            number_locations.extend(numbers)
        multiplier_locations.extend(find_multipliers(line, row))
    for number in number_locations:
        if adjacent_symbol(data, number):
            number_sum += number[0]
    print(f"Part I - Part Number Sum = {number_sum}")

    gear_total = 0
    for multiplier in multiplier_locations:
        number_list = []
        for number in number_locations:
            # it's a little clinky working out the valid range of positions that are adjacent to the multiplier
            if multiplier[0] >= number[1] - 1 and multiplier[0] <= number[1] + 1:
                if multiplier[1] >= number[2][0] - 1 and multiplier[1] <= number[2][1]:
                    number_list.append(number[0])
        if len(number_list) == 2:
            gear_total += number_list[0] * number_list[1]
    print(f"Part II - Grear Total = {gear_total}")


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

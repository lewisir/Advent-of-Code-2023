"""
--- Advent of Code 2023 ---
--- Day 1: Trebuchet?! ---
https://adventofcode.com/2023/day/1
"""

from time import perf_counter

TEST = False

DAY = "1"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT


DIGITS_I = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

DIGITS = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_input_data(filename):
    """function to read in the input data"""
    file_data = []
    with open(filename) as file:
        for line in file:
            file_data.append(line.rstrip("\n"))
    return file_data


def reverse_string(text):
    """returns a string in revese order"""
    reversed_string = ""
    for i in range(-1, -len(text) - 1, -1):
        reversed_string += text[i]
    return reversed_string


def find_first_digit(data):
    """return the value of the value of the first digit in the string, return None if no digit is found"""
    for position, char in enumerate(data):
        if char in DIGITS_I:
            return char
    return None


def find_last_digit(data):
    """return the value of the value of the last digit in the string, return None if no digit is found"""
    last_position = -1
    last_digit = "x"
    for position, char in enumerate(data):
        if char in DIGITS_I:
            last_position = position
            last_digit = char
    if last_position == -1:
        return None
    else:
        return last_digit


def find_first_number(data):
    """Find the first number in the string input and return it's value, or return None if it is not found"""
    position = len(data) + 1
    first_number = "x"
    for number in DIGITS:
        result = data.find(number)
        if result > -1 and position > result:
            position = result
            first_number = number
    if first_number != "x":
        return first_number
    else:
        return None


def find_last_number(data):
    """Find the last number in the string input and return it's value, or return None if it is not found"""
    position = -1
    last_number = "x"
    for number in DIGITS:
        result = data.rfind(number)
        if result > -1 and position < result:
            position = result
            last_number = number
    if last_number != "x":
        return last_number
    else:
        return None


def convert_word_to_number(word):
    """if the word is a number then return the string of the digit; e.g. 'two' returns '2'"""
    if word in NUMBERS:
        return NUMBERS[word]
    else:
        return word


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    calibration_sum = 0
    for line in data:
        first = find_first_digit(line)
        last = find_last_digit(line)
        if first is not None and last is not None:
            calibration_value = int(first + last)
        calibration_sum += calibration_value
    print(f"Part I - Total Calibration = {calibration_sum}")

    calibration_sum = 0
    for line in data:
        first = convert_word_to_number(find_first_number(line))
        last = convert_word_to_number(find_last_number(line))
        if first is not None and last is not None:
            calibration_value = int(first + last)
        calibration_sum += calibration_value
    print(f"Part II - Total Calibration = {calibration_sum}")


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

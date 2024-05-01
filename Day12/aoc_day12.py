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
MEMO = {}
MEMOIZE = False


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    # calculate(data)
    compare(data)

    # Odd, but if I pass in a list rather than a tuple to permute_string I get a wrong answer in some cases
    # try permute_string("????.#...#...", [4, 1, 1]) gives result 0 rather than 1


def calculate(data):
    """Calculate the total number of variations"""
    count = 0
    for line in data:
        spring_string, damaged_data = line.split(" ")
        damaged_data = damaged_data.split(",")
        damaged_data = tuple([int(x) for x in damaged_data])
        spring_string = grow_string(spring_string, MULTIPLIER)
        damaged_data = damaged_data * MULTIPLIER
        count += short_perm_string(spring_string, damaged_data)
    print(f"Count = {count}")


def compare(data):
    """Output the comparative counts of the two permute functions"""
    print(f"String\tData\tShort_Perm\tPermute")
    for line in data:
        spring_string, damaged_data = line.split(" ")
        damaged_data = damaged_data.split(",")
        damaged_data = tuple([int(x) for x in damaged_data])
        spring_string = grow_string(spring_string, MULTIPLIER)
        damaged_data = damaged_data * MULTIPLIER
        short = short_perm_string(spring_string, damaged_data)
        long = permute_string(spring_string, damaged_data)
        if short != long:
            print(f"{spring_string}\t{damaged_data}\t{short}\t{long}")


def permute_string(input_string, damaged_data, count=0):
    """Recursively calculate the number of permutation of the given string and damaged spring data"""
    next_qm = input_string.find("?")
    # If there is a '?' then work out if we can replace with it '.' and/or '#'
    if next_qm > -1:
        first_section = input_string[:next_qm]
        second_section = input_string[next_qm + 1 :]
        first_section_damaged_data = calculate_damaged_spring_data(first_section)
        remaining_damaged_data = subtract_sequences(
            damaged_data, first_section_damaged_data
        )
        qm_credit = (
            input_string.count("?") - sum(damaged_data) + input_string.count("#")
        )
        # always check if there are enough '?' for the remaining '#' (qm_credt >= 0)
        # check if the start of the input string is 'good' and if so replace '?' with '.' and pass to permute_string
        if match_sequences(first_section_damaged_data, damaged_data) and qm_credit >= 0:
            if MEMOIZE and (second_section, remaining_damaged_data) in MEMO.keys():
                count += MEMO[(second_section, remaining_damaged_data)]
            else:
                new_string = first_section + "." + second_section
                old_count = count
                count = permute_string(new_string, damaged_data, count)
                if MEMOIZE:
                    MEMO[(second_section, remaining_damaged_data)] = count - old_count
        # replace '?' with '#' and pass to permute_string
        if qm_credit >= 0:
            new_string = first_section + "#" + second_section
            count = permute_string(new_string, damaged_data, count)
    # If there's no '?' test whether we have a valid string
    else:
        if calculate_damaged_spring_data(input_string) == damaged_data:
            count += 1
    return count


def short_perm_string(input_string, damaged_data, count=0):
    """Recursively calculate the number of perumtations of the given string and damaged spring data"""
    next_qm = input_string.find("?")
    if next_qm > -1:
        first_section = input_string[:next_qm]
        second_section = input_string[next_qm + 1 :]
        first_section_damaged_data = calculate_damaged_spring_data(first_section)
        remaining_damaged_data = subtract_sequences(
            damaged_data, first_section_damaged_data
        )
        qm_credit = (
            input_string.count("?") - sum(damaged_data) + input_string.count("#")
        )
        if match_sequences(first_section_damaged_data, damaged_data) and qm_credit >= 0:
            count = short_perm_string(second_section, remaining_damaged_data, count)
        if qm_credit >= 0:
            new_string = first_section + "#" + second_section
            count = short_perm_string(new_string, damaged_data, count)
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


def reduce_dots(input_string):
    """Redcue consecutive sequences of '.' to a single '.' and return the string"""
    ouput_string = ""
    found_dot = False
    for c in input_string:
        if c == "." and found_dot == False:
            found_dot = True
            ouput_string += c
        elif c != ".":
            found_dot = False
            ouput_string += c
    return ouput_string


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

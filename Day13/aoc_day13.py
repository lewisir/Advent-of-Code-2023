"""
--- Advent of Code 2023 ---
--- Day 13: Point of Incidence ---
https://adventofcode.com/2023/day/13
"""

from time import perf_counter
from pprint import pprint

TEST = False

DAY = "13"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    collection_of_patterns = process_input_data(data)
    summary_score = 0
    for pattern in collection_of_patterns:
        horizonal_match = search_for_mirror(pattern)
        vertical_match = search_for_mirror(transpose(pattern))
        if horizonal_match is not None:
            summary_score += 100 * horizonal_match
        elif vertical_match is not None:
            summary_score += vertical_match
    print(f"Part I Summary Score = {summary_score}")


def search_for_mirror(pattern):
    """given the pattern search for a line of symmetry returning the number of entries before the symmetry line"""
    for i in range(1, len(pattern)):
        seq1, seq2 = split_list(pattern, i)
        seq1.reverse()
        comparison_result = compare_sequences(seq1, seq2)
        if comparison_result == i or comparison_result == len(pattern) - i:
            return i


def process_input_data(data):
    """process the input and store each pattern in a list"""
    collection_of_patterns = []
    new_pattern = []
    for line in data:
        if line == "":
            collection_of_patterns.append(new_pattern)
            new_pattern = []
        else:
            new_pattern.append(line)
    collection_of_patterns.append(new_pattern)
    return collection_of_patterns


def compare_sequences(seq1, seq2):
    """In order, compare the items in sequence 1 and sequence 2.
    Return the number of items that match between the two sequences
    A return value of 0 means that the first items are different.
    A value of 3 means the first 3 items are the same and the 4th is different"""
    length = min(len(seq1), len(seq2))
    count = 0
    for i in range(0, length):
        if seq1[i] == seq2[i]:
            count += 1
    return count


def transpose(matrix):
    """Given a 2 dimensional matrix, return a new transposed matrix"""
    return [list(x) for x in zip(*matrix)]


def split_list(sequence, position):
    """given a sequence, split it at the position provided and return the two sequences"""
    seq1 = sequence[:position]
    seq2 = sequence[position:]
    return seq1, seq2


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

"""
--- Advent of Code 2023 ---
--- Day 14: Parabolic Reflector Dish ---
https://adventofcode.com/2023/day/14
"""

from time import perf_counter
from pprint import pprint

TEST = True

DAY = "14"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT


def main():
    """Main program"""
    # data = get_input_data(FILENAME)
    data = ['O....#....','O.OO#....#']
    platform = rotate(data)
    platform = tilt(platform)
    print(f"Part I Load = {total_load(platform)}")

    # Not figured an efficient way to do Part II yet
    # figure out the weight after each cycle and store in a list
    # but this produces a pattern that does not result in a test weight of 64???
    platform = data
    weight_list = []
    for i in range(100):
        platform = cycle(platform)
        weight_list.append(total_load(platform))
    print(find_patterns([1,2,3,4,5,6,2,3,4,2,3,4,2,3,4]))

def find_patterns(number_list):
    """Given a list of integers locate a repeating pattern"""
    max_found_len = 0
    for offset in range(len(number_list)//2):
        for pattern_length in range(2,len(number_list)//3):
            found_list = find_sub_list(number_list,number_list[offset:offset+pattern_length],offset)
            if len(found_list) > max_found_len:
                max_found_len = len(found_list)
                max_found_sub = found_list
    return max_found_sub

def find_sub_list(main_list, sub_list, start=0):
    """Find the sub_list in the main_list and return it's starting index position"""
    found_list = []
    for s in sub_list:
        search_result = main_list.index(s,start)
        if search_result >= 0:
            found_list.append(search_result)
    return found_list

def cycle(platform, number = 1):
    """tilt the platform through all four directions"""
    for _ in range(number*4):
        platform = rotate(platform)
        platform = tilt(platform)
    return platform

def tilt(platform):
    """tilt the platform to the 'north' and return the new platform"""
    for i,line in enumerate(platform):
        platform[i] = roll_across_line(line)
    return platform

def total_load(platform):
    """calculate the total load on the platform"""
    load = 0
    for line in platform:
        load += line_weight(line)
    return load

def line_weight(line):
    """calculate the weight of a single line"""
    weight = 0
    for i,s in enumerate(line):
        if s == 'O':
            weight += i+1
    return weight

def rotate(matrix):
    """Given a 2 dimensional matrix, return a new 90 degree rotated matrix"""
    return [''.join(list(x)) for x in zip(*matrix[::-1])]

def roll_across_line(line):
    """Given a row or fixed rocks '#' and rolling rocks 'O', roll all the rocks across to the right"""
    sub_strings = line.split('#')
    for i,s in enumerate(sub_strings):
        sub_strings[i] = right_justify(s)
    return '#'.join(sub_strings)

def right_justify(line):
    """move all the 'O' to the left hand side of the input line"""
    num_rocks = line.count('O')
    return '.'*(len(line)-num_rocks) + 'O'*num_rocks

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

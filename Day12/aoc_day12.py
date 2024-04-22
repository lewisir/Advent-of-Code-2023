"""
--- Advent of Code 2023 ---
--- Day 12: Hot Springs ---
https://adventofcode.com/2023/day/12
"""

from time import perf_counter
import itertools
import sys
import pprint

TEST = False

DAY = "12"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT

INDENT = 4

MULTIPLIER = 2

MEMO = {}

def main():
    """Main program"""
    data = get_input_data(FILENAME)
    result_list = []
    # alternative = 0
    """
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
        # alternative += total_perms(spring_data, damaged_springs)
    alternative = sum(result_list)
    print(f"Part 1 - sum of alternatives = {alternative}")
    """
    # Part I works but is slow (about 5 seconds)
    # And if I call total_perms instead, it's even slower?????
    # New approach is to work through the string section by section (delimited by groups of '#') and check as we go whether we're producing a string that will match the damaged spring summary data 
    # print(f"Testing Perumte Count = {permute_string('?.#.?..?#?.?',0,[1,1,1,1])}")
    # print(f"first method with '.??..??...?##.' Count = {total_perms('.??..??...?##.',[1,1,3])}")
    # print(f"secnd method with '.??..??...?##.' Count = {permute_string('.??..??...?##.',0,[1,1,3])}")
    # print(f"first method with '.??..??...?##...??..??...?##...??..??...?##...??..??...?##.' Count = {total_perms('.??..??...?##...??..??...?##...??..??...?##...??..??...?##.',[1,1,3,1,1,3,1,1,3,1,1,3])}")
    # print(f"secnd method with '.??..??...?##...??..??...?##...??..??...?##...??..??...?##.' Count = {permute_string('.??..??...?##...??..??...?##...??..??...?##...??..??...?##.',0,[1,1,3,1,1,3,1,1,3,1,1,3])}")

    """
    count = 0
    for line in data:
        spring_data, damaged_springs = line.split(" ")
        damaged_springs = damaged_springs.split(",")
        damaged_springs = [int(x) for x in damaged_springs]
        spring_data = grow_string(spring_data,MULTIPLIER)
        damaged_springs = damaged_springs * MULTIPLIER
        print(f"working {spring_data} with {damaged_springs}")
        count += permute_string(spring_data,0,damaged_springs)
        print(f"Running count {count}")
    """

    # print(f"Permute '?#?#?#?#?#?#?#?' [1,3,1,6] gives {permute_string('?#?#?#?#?#?#?#?',0,[1,3,1,6])} permutations")
    # print(f"Permute '?#?#' [3] gives {permute_string('?#?#',0,[3])} permutations")
    # print(f"Extract '?#?#' {extract_next_section('?#?#',0)}")

    #count = perm_string('?#?#?#?#?#?#?#?',[1,3,1,6])
    #print(f"Counting Perms of '?#?#?#?#?#?#?#?' [1,3,1,6] = {count}")

    count = 0
    
    for line in data:
        spring_data, damaged_springs = line.split(" ")
        spring_data = trim_dots(spring_data)
        damaged_springs = damaged_springs.split(",")
        damaged_springs = [int(x) for x in damaged_springs]
        spring_data = grow_string(spring_data,MULTIPLIER)
        damaged_springs = damaged_springs * MULTIPLIER
        count += perm_string(spring_data,damaged_springs)

    print(f"Valid Alternatives = {count}")
    pprint.pprint(MEMO)
   

def perm_string(input_string,damaged_data,count=0):
    """recursively find all the possible spring arrangements"""
    #if MEMO.get((input_string,str(damaged_data))):
    #    return MEMO[(input_string,str(damaged_data))]
    #else:
    if input_string.find("?") > -1:
        next_section = input_string[:input_string.find('?')+1]
        temp_damaged_data = calculate_number_record(next_section[:-1])
        # print(f"Debug:\tInput:\t{input_string}\tData:\t{damaged_data}\n\tNext:\t{next_section}\tTemp:\t{temp_damaged_data}")
        if compare_lists(temp_damaged_data,damaged_data):
            # print(f"  Debug: Call with {"."+input_string[len(next_section):]} and {subtract_list(damaged_data,temp_damaged_data)}")
            count = perm_string(trim_dots("."+input_string[len(next_section):]),subtract_list(damaged_data,temp_damaged_data),count)
#            MEMO[(input_string,str(damaged_data))] = count
        if input_string.count('#') >= sum(damaged_data):
            return count
        else:
            count = perm_string(merge_strings(input_string,next_section[:-1]+"#"),damaged_data,count)
#            MEMO[(input_string,str(damaged_data))] = count
    else:
        if calculate_number_record(input_string) == damaged_data:
            count += 1
        return count
    return count



def total_perms(spring_string, damaged_springs):
    """caclulate the number of permissable combinations of the spring_string"""
    count = 0
    unknown_spring_locations = find_char_positions(spring_string, "?")
    possible_damaged_springs = produce_combinations(unknown_spring_locations,sum(damaged_springs) - spring_string.count("#"))
    for possible in possible_damaged_springs:
        test_string = create_spring_data(spring_string,possible)
        if get_damaged_springs(test_string) == damaged_springs:
            count += 1
    return count


def permute_string(spring_string, n, damaged_springs, perm_count=0):
    """calcualte the number of permissable combinations of the spring_string"""
    if n == len(spring_string) and calculate_number_record(spring_string) == damaged_springs:
        #print(f"incrementing perm_count by 1 from {perm_count}")
        perm_count += 1
        return perm_count
    elif n == len(spring_string):
        #print(f"returning perm_count {perm_count} as n == len(spring_string)")
        return perm_count
    next_section = extract_next_section(spring_string,n)
    n = len(next_section)
    unknown_spring_locations = find_char_positions(next_section,"?")
    possible_springs = min(sum(damaged_springs)-spring_string.count("#"),next_section.count("?"))
    #print(f"Data\n\tnext_section\t{next_section}\n\tunknown_spring_locations\t{unknown_spring_locations}\n\tpossible_springs\t{possible_springs}")
    combinations = produce_combinations(unknown_spring_locations,possible_springs)
    for possible in combinations:
        new_string = create_spring_data(next_section,possible)
        new_data = calculate_number_record(new_string)
        if compare_lists(new_data,damaged_springs):
            perm_count = permute_string(merge_strings(spring_string,new_string),n,damaged_springs, perm_count)
    return perm_count

def trim_dots(spring_string):
    """
    Remove consecutice sequences of '.' from the string, reducing them to a single '.'
    Also remove leading or trailing '.'
    """
    output_string = ''
    found_dot = False
    for char in spring_string:
        if char != '.':
            output_string += char
            found_dot = False
        elif char == '.' and not found_dot:
            output_string += char
            found_dot = True
    output_string = remove_end_dots(output_string)
    return output_string

def remove_end_dots(spring_string):
    """Remove any leading or trailing dots"""
    if spring_string[0] == '.':
        start = 1
    else:
        start = 0
    if spring_string[-1] == '.':
        end = -1
    else:
        end = None
    return spring_string[start:end]


def subtract_list(list1, list2):
    """return a list that is the result of removing the items in list 2 from the the items in list1 where list 2 is euqal to the start of list1"""
    if len(list1) < len(list2):
        return None
    elif list1[:len(list2)] != list2:
        return None
    else:
        return list1[len(list2):]

def merge_strings(full_string, start_string):
    """replace the start of the full_string with the start_string"""
    return start_string+full_string[len(start_string):]

def extract_next_section(spring_string, n):
    """
    Starting at index position n, extract the next section of the spring_string up to include the next contiguous block of '?'
    unless the end of the string is reached in which case return the whole string
    include any contiguous blocks of '#' that are adjacent to the block of '?'
    """
    output_string = spring_string[:n]
    found_unknown = False
    found_hash = False
    for i in range(n,len(spring_string)):
        char = spring_string[i]
        output_string += char
        if char == '?':
            found_unknown = True
            #print(f"found_unknown at {i} '{spring_string[i]}' found_unknown = {found_unknown}")
            if found_hash:
                print(f"     also found_hash = {found_hash} and returning '{output_string}'")
                return output_string
                # return spring_string[:n+i]
        elif char == '#' and found_unknown:
            #print(f"found_hash at {i} '{spring_string[i]}' found_hash = {found_hash}")
            found_hash = True
        elif char == '.' and found_unknown:
            #print(f"found '.' at {i} '{spring_string[i]}' and returning '{output_string}")
            return output_string
            # return spring_string[:n+i]
    #print(f"reached end and returning '{output_string}")
    return output_string
    #return spring_string[:n+i]



def calculate_number_record(spring_string):
    """Calculate the number of damaged springs in each contiguous group and return the list of the numbers"""
    count = 0
    number_record = []
    for c in spring_string:
        if c == '#':
            count +=1
        elif c == '.' and count > 0:
            number_record.append(count)
            count = 0
    if count > 0:
        number_record.append(count)
    return number_record

def compare_lists(list1,list2):
    """Compare the two lists and return true if all the items in the shorter list appear in order at the start of the longer list"""
    if list1 is None or list2 is None:
        print(f"List error {list1} {list2}")
        sys.exit()
    if len(list1) <= len(list2):
        short_list = list1
        long_list = list2
    else:
        short_list = list2
        long_list = list1
    for index, item in enumerate(short_list):
        if long_list[index] != item:
            return False
    return True

def produce_combinations(array,n):
    """Return all the subsets of array that have 0 to n elements in them"""
    output = []
    for i in range(n+1):
        combi = itertools.combinations(array,i)
        for combination in combi:
            output.append(combination)
    return output


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

def grow_string(input_string,n,separator='?'):
    """return the input_string n times with each occurance separated by the separator"""
    output_string = input_string
    for _ in range(n-1):
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

"""
--- Advent of Code 2023 ---
--- Day 15: Lens Library ---
https://adventofcode.com/2023/day/15
"""

from time import perf_counter
from pprint import pprint

TEST = False

DAY = "15"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    initialization_sequence = data[0].split(",")
    hash_sum = 0
    for step in initialization_sequence:
        hash_sum += hash(step)

    print(f"Part I Hash Sum is {hash_sum}")

    boxes = {}
    for step in initialization_sequence:
        lens = extract_lens_info(step)
        box = hash(lens["label"])
        if lens["focal_length"] > 0:
            boxes = add_lens(boxes, box, lens)
        else:
            boxes = remove_lens(boxes, box, lens)

    print(f"Part II focal power = {focussing_power(boxes)}")


def add_lens(boxes, box, lens_to_add):
    """Add to the box the lens in the right most position or replace the lens if it already exists"""
    if box not in boxes.keys():
        boxes[box] = []
    for index, lens in enumerate(boxes[box]):
        if lens["label"] == lens_to_add["label"]:
            boxes[box][index] = lens_to_add
            return boxes
    boxes[box].append(lens_to_add)
    return boxes


def remove_lens(boxes, box, lens_to_remove):
    """Remove the lens, if it exists, from the box"""
    try:
        for index, lens in enumerate(boxes[box]):
            if lens["label"] == lens_to_remove["label"]:
                del boxes[box][index]
        return boxes
    except:
        return boxes


def extract_lens_info(lens_text):
    """Return the lens label and focal length, use -1 if the action is to remove the lens"""
    if lens_text.find("=") > 0:
        return {"label": lens_text[:-2], "focal_length": int(lens_text[-1])}
    else:
        return {"label": lens_text[:-1], "focal_length": -1}


def focussing_power(boxes):
    """Calculate the power of the boxes"""
    power = 0
    for box in boxes:
        for position, lens in enumerate(boxes[box]):
            power += (box + 1) * (position + 1) * lens["focal_length"]
    return power


def hash(input_string):
    """Return the hash value of the input string"""
    value = 0
    for s in input_string:
        value += ord(s)
        value *= 17
        value = value % 256
    return value


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

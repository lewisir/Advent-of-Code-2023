"""
--- Advent of Code 2023 ---
--- Day 4: Scratchcards ---
https://adventofcode.com/2023/day/4
"""

from time import perf_counter

TEST = False

DAY = "4"
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


def count_wins(winning_nos, played_nos):
    """count how many times each winning number occurs in the played numbers"""
    count = 0
    for number in winning_nos:
        if number in played_nos:
            count += 1
    return count


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    points = 0
    card_totals = {}
    for card in data:
        card_name, number_data = card.split(":")
        card_id = int(card_name[5:])
        winning_numbers, played_numbers = number_data.split("|")
        wins = count_wins(winning_numbers.split(), played_numbers.split())
        card_totals[card_id] = {"wins": wins, "total": 1}
        if wins > 0:
            points += 2 ** (wins - 1)
    print(f"Part I -  Points Total = {points}")

    for card in card_totals:
        wins = card_totals[card]["wins"]
        if wins > 0:
            for i in range(card + 1, card + wins + 1):
                card_totals[i]["total"] += card_totals[card]["total"]

    card_sum = 0
    for card in card_totals:
        card_sum += card_totals[card]["total"]
    print(f"Part II - Card total = {card_sum}")


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

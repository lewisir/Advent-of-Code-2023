"""
--- Advent of Code 2023 ---
--- Day 7: Camel Cards ---
https://adventofcode.com/2023/day/7
"""

from time import perf_counter
import pprint

TEST = False

DAY = "7"
REAL_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_day" + DAY + ".txt"
TEST_INPUT = "Advent-of-Code-2023/Day" + DAY + "/input_test.txt"

if TEST:
    FILENAME = TEST_INPUT
else:
    FILENAME = REAL_INPUT

CARDS = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}
CARDS_II = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}
TYPES = {"5K": 6, "4K": 5, "FH": 4, "3K": 3, "2P": 2, "1P": 1, "HC": 0}


def get_input_data(filename):
    """function to read in the input data"""
    file_data = []
    with open(filename) as file:
        for line in file:
            file_data.append(line.rstrip("\n"))
    return file_data


def hand_type(hand, joker=False):
    """Given a card hand, return the type of hand"""
    card_counts = []
    joker_count = 0
    if joker:
        joker_count = hand.count("J")
    for card in hand:
        current_card_count = hand.count(card)
        card_counts.append(current_card_count)
    card_counts.sort()
    if card_counts == [1, 1, 1, 1, 1]:
        if joker_count == 1:
            return "1P"
        else:
            return "HC"
    if card_counts == [1, 1, 1, 2, 2]:
        if joker_count == 1:
            return "3K"
        elif joker_count == 2:
            return "3K"
        else:
            return "1P"
    if card_counts == [1, 2, 2, 2, 2]:
        if joker_count == 1:
            return "FH"
        elif joker_count == 2:
            return "4K"
        else:
            return "2P"
    if card_counts == [2, 2, 3, 3, 3]:
        if joker_count == 2:
            return "5K"
        elif joker_count == 3:
            return "5K"
        else:
            return "FH"
    if card_counts == [1, 1, 3, 3, 3]:
        if joker_count == 1:
            return "4K"
        elif joker_count == 3:
            return "4K"
        else:
            return "3K"
    if card_counts == [1, 4, 4, 4, 4]:
        if joker_count > 0:
            return "5K"
        else:
            return "4K"
    if card_counts == [5, 5, 5, 5, 5]:
        return "5K"


def rank_hands(hand1, hand2, joker=False):
    """compare the two hands and return True if hand1 is better than hand2, return False if not"""
    if joker:
        cards = CARDS_II
    else:
        cards = CARDS
    comp = iter(zip(hand1, hand2))
    for pair in comp:
        if cards[pair[0]] > cards[pair[1]]:
            return True
        elif cards[pair[0]] < cards[pair[1]]:
            return False


def main():
    """Main program"""
    data = get_input_data(FILENAME)
    hands = {}
    for line in data:
        hand, bid = line.split()
        hands[hand] = {
            "bid": int(bid),
            "type_rank": TYPES[hand_type(hand)],
            "type_joker_rank": TYPES[hand_type(hand, True)],
        }
    # pprint.pprint(hands)

    ordered_hands = []
    for type in range(0, 7):
        temp_hand_list = []
        for hand in hands:
            if hands[hand]["type_rank"] == type:
                temp_hand_list.append(hand)
        if len(temp_hand_list) > 1:
            sorted = False
            while not sorted:
                swapped = False
                for index in range(len(temp_hand_list)):
                    if index == len(temp_hand_list) - 1:
                        if swapped == False:
                            sorted = True
                        break
                    elif rank_hands(temp_hand_list[index], temp_hand_list[index + 1]):
                        hand1 = temp_hand_list[index]
                        hand2 = temp_hand_list[index + 1]
                        temp_hand_list[index] = hand2
                        temp_hand_list[index + 1] = hand1
                        swapped = True
        ordered_hands.extend(temp_hand_list)
    # pprint.pprint(ordered_hands)

    winnings = 0
    for rank, hand in enumerate(ordered_hands):
        winnings += hands[hand]["bid"] * (rank + 1)

    print(f"Part I - winnings = {winnings}")

    ordered_hands = []
    for type in range(0, 7):
        temp_hand_list = []
        for hand in hands:
            if hands[hand]["type_joker_rank"] == type:
                temp_hand_list.append(hand)
        if len(temp_hand_list) > 1:
            sorted = False
            while not sorted:
                swapped = False
                for index in range(len(temp_hand_list)):
                    if index == len(temp_hand_list) - 1:
                        if swapped == False:
                            sorted = True
                        break
                    elif rank_hands(
                        temp_hand_list[index], temp_hand_list[index + 1], True
                    ):
                        hand1 = temp_hand_list[index]
                        hand2 = temp_hand_list[index + 1]
                        temp_hand_list[index] = hand2
                        temp_hand_list[index + 1] = hand1
                        swapped = True
        ordered_hands.extend(temp_hand_list)

    pprint.pprint(ordered_hands)

    winnings = 0
    for rank, hand in enumerate(ordered_hands):
        winnings += hands[hand]["bid"] * (rank + 1)

    print(f"Part II - winnings = {winnings}")

    # First attempt, 255564938 is too low ???


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(f"-- Time Taken {perf_counter() - start_time}")

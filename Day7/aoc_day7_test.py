import aoc_day7


def test_hand_type():
    """Test the classification of the poker hands"""
    assert aoc_day7.hand_type("23456", False) == "HC"
    assert aoc_day7.hand_type("23426", False) == "1P"
    assert aoc_day7.hand_type("23626", False) == "2P"
    assert aoc_day7.hand_type("26626", False) == "FH"
    assert aoc_day7.hand_type("66626", False) == "4K"
    assert aoc_day7.hand_type("88888", False) == "5K"
    assert aoc_day7.hand_type("23J56", True) == "1P"
    assert aoc_day7.hand_type("2J426", True) == "3K"
    assert aoc_day7.hand_type("2J626", True) == "FH"
    assert aoc_day7.hand_type("J3J56", True) == "3K"
    assert aoc_day7.hand_type("J3JJ6", True) == "4K"
    assert aoc_day7.hand_type("JJJJ6", True) == "5K"

# Tests for Day 12

import pytest
import aoc_day12


def test_calculate_damaged_spring_data():
    assert aoc_day12.calculate_damaged_spring_data("#.#.###") == (1, 1, 3)
    assert aoc_day12.calculate_damaged_spring_data(".#...#....###.") == (1, 1, 3)
    assert aoc_day12.calculate_damaged_spring_data(".#.###.#.######") == (1, 3, 1, 6)
    assert aoc_day12.calculate_damaged_spring_data("####.#...#...") == (4, 1, 1)
    assert aoc_day12.calculate_damaged_spring_data("#....######..#####.") == (1, 6, 5)
    assert aoc_day12.calculate_damaged_spring_data("#.#.###") == (1, 1, 3)
    assert aoc_day12.calculate_damaged_spring_data(".###.##....#") == (3, 2, 1)


def test_match_sequences():
    assert aoc_day12.match_sequences((1, 2, 3), (1, 2, 3)) == True
    assert aoc_day12.match_sequences((1, 2, 3, 4, 5, 6), (1, 2, 3)) == True
    assert aoc_day12.match_sequences((1, 2, 3), (1, 2, 3, 4, 5)) == True
    assert aoc_day12.match_sequences((1, 2, 3), ()) == True
    assert aoc_day12.match_sequences((), (1, 2, 3)) == True
    assert aoc_day12.match_sequences((1, 8, 3), (1, 2, 3)) == False
    assert aoc_day12.match_sequences((1, 2, 3, 4, 5, 6), (1, 2, 3, 8)) == False
    assert aoc_day12.match_sequences((), ()) == True


def test_subtract_sequences():
    assert aoc_day12.subtract_sequences((1, 2, 3), (1, 2, 3, 4)) == (4,)
    assert aoc_day12.subtract_sequences((1, 2, 3, 4, 5, 6), (1, 2, 3, 4)) == (5, 6)
    assert aoc_day12.subtract_sequences((), ()) == ()
    assert aoc_day12.subtract_sequences((1, 2, 3), (1, 2, 3)) == ()
    assert aoc_day12.subtract_sequences((1, 8, 3), (1, 2, 3, 4)) == None


def test_reduce_dots():
    assert aoc_day12.reduce_dots(".#.#.?.#.#.?.") == ".#.#.?.#.#.?."
    assert aoc_day12.reduce_dots("..#.#.?.#.#.?.") == ".#.#.?.#.#.?."
    assert aoc_day12.reduce_dots(".#.#.?.#.#.?..") == ".#.#.?.#.#.?."
    assert aoc_day12.reduce_dots(".#.#.?...#.#.?.") == ".#.#.?.#.#.?."
    assert aoc_day12.reduce_dots(".#....#.?.#.#....?.") == ".#.#.?.#.#.?."


def test_permute_string():
    assert aoc_day12.permute_string("???.###", (1, 1, 3)) == 1
    assert aoc_day12.permute_string(".??..??...?##.", (1, 1, 3)) == 4
    assert aoc_day12.permute_string("????.#...#...", (4, 1, 1)) == 1
    assert aoc_day12.permute_string("????.######..#####.", (1, 6, 5)) == 4
    assert aoc_day12.permute_string("?###????????", (3, 2, 1)) == 10
    assert aoc_day12.permute_string("?#?#?#?#?#?#?#?", (1, 3, 1, 6)) == 1
    assert aoc_day12.permute_string("?.", (1,)) == 1
    assert aoc_day12.permute_string(".?", (1,)) == 1
    assert aoc_day12.permute_string("??", (1,)) == 2
    assert aoc_day12.permute_string("??", (2,)) == 1

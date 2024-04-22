# Tests for Day 12

import pytest
import aoc_day12

def test_calculate_number_record():
    assert aoc_day12.calculate_number_record('#.#.###') == [1,1,3]
    assert aoc_day12.calculate_number_record('.#...#....###.') == [1,1,3]
    assert aoc_day12.calculate_number_record('.#.###.#.######') == [1,3,1,6]
    assert aoc_day12.calculate_number_record('####.#...#...') == [4,1,1]
    assert aoc_day12.calculate_number_record('#....######..#####.') == [1,6,5]
    assert aoc_day12.calculate_number_record('#.#.###') == [1,1,3]
    assert aoc_day12.calculate_number_record('.###.##....#') == [3,2,1]

def test_compare_lists():
	assert aoc_day12.compare_lists([1,2,3],[1,2,3,4,5]) == True
	assert aoc_day12.compare_lists([1,2,3,4,5,6],[1,2,3,4]) == True
	assert aoc_day12.compare_lists([1,2,3,4,5,6],[1,2,3,4,5,6]) == True
	assert aoc_day12.compare_lists([1,2,3],[2,2,3,4,5]) == False
	assert aoc_day12.compare_lists([1,2,4],[1,2,3,4,5]) == False
	assert aoc_day12.compare_lists([1,2,3,4,5,6],[1,6,3]) == False
	assert aoc_day12.compare_lists([],[1,2]) == True

def test_extract_next_section():
	assert aoc_day12.extract_next_section('???.###',0) == '???.'
	assert aoc_day12.extract_next_section('???.###',3) == '???.###'
	assert aoc_day12.extract_next_section('???.###',4) == '???.###'
	assert aoc_day12.extract_next_section('.??..??...?##.',0) == '.??.'
	assert aoc_day12.extract_next_section('.??..??...?##.',4) == '.??..??.'
	assert aoc_day12.extract_next_section('.??..??...?##.',8) == '.??..??...?##.'

def test_merge_strings():
	assert aoc_day12.merge_strings('abcdefghi','12345') == '12345fghi'

def test_permute_string():
	assert aoc_day12.permute_string('???.###',0,[1,1,3]) == 1
	assert aoc_day12.permute_string('.??..??...?##.',0,[1,1,3]) == 4
	#assert aoc_day12.permute_string('?#?#?#?#?#?#?#?',0,[1,3,1,6]) == 1
	assert aoc_day12.permute_string('????.#...#...',0,[4,1,1]) == 1
	assert aoc_day12.permute_string('????.######..#####.',0,[1,6,5]) == 4
	assert aoc_day12.permute_string('?###????????',0,[3,2,1]) == 10
	assert aoc_day12.permute_string('?.',0,[1]) == 1
	assert aoc_day12.permute_string('.?',0,[1]) == 1
	assert aoc_day12.permute_string('??',0,[1]) == 2
	assert aoc_day12.permute_string('??',0,[2]) == 1
	assert aoc_day12.permute_string('??',0,[2]) == 1

def test_trim_dots():
	assert aoc_day12.trim_dots(".?.?.?") == "?.?.?"
	assert aoc_day12.trim_dots("..?.?") == "?.?"
	assert aoc_day12.trim_dots(".?.##...##...#..?.?") == "?.##.##.#.?.?"
	assert aoc_day12.trim_dots(".?.?.?.....") == "?.?.?"


def test_subtract_list():
	assert aoc_day12.subtract_list([1,2,3,4,5],[1,2,3]) == [4,5]
	assert aoc_day12.subtract_list([1,2],[1,2,3]) == None
	assert aoc_day12.subtract_list([1,7,3,4,5],[1,2,3]) == None
	assert aoc_day12.subtract_list([1,7,3,4,5],[]) == [1,7,3,4,5]

def test_remove_end_dots():
	assert aoc_day12.remove_end_dots('.#.?##?.') == '#.?##?'
	assert aoc_day12.remove_end_dots('#.?##?') == '#.?##?'




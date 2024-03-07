# Tests for Day 5

import pytest
import aoc_day5

def test_mapping():
	assert aoc_day5.split_range((55,13),{"src_start": 1, "dst_start": 10, "map_range": 2}) == ([(55,13)],[])
	assert aoc_day5.split_range((55,13),{"src_start": 54, "dst_start": 10, "map_range": 4}) == ([(58,10)],[(11,3)])
	assert aoc_day5.split_range((55,13),{"src_start": 65, "dst_start": 10, "map_range": 4}) == ([(55,10)],[(10,3)])
	assert aoc_day5.split_range((55,13),{"src_start": 58, "dst_start": 10, "map_range": 4}) == ([(55,3),(62,6)],[(10,4)])



"""
Examples
(55,13) - 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67
map_from - 58, 59, 60, 61
map_to   - 10, 11, 12, 13

(55,3),(62,6)
(10,4)

"""

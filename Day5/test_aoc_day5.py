# Tests for Day 5

import pytest
import aoc_day5

def test_mapping():
	# Do not mathc the range (map ends lower than the start or igher than the end of the range)
	assert aoc_day5.split_range((55,13),{"src_start": 1, "dst_start": 10, "map_range": 2}) == ([(55,13)],[])
	assert aoc_day5.split_range((55,13),{"src_start": 91, "dst_start": 10, "map_range": 3}) == ([(55,13)],[])

	# Match the start or the end of the range
	assert aoc_day5.split_range((55,13),{"src_start": 54, "dst_start": 10, "map_range": 4}) == ([(58,10)],[(11,3)])
	assert aoc_day5.split_range((55,13),{"src_start": 65, "dst_start": 10, "map_range": 4}) == ([(55,10)],[(10,3)])

    # Match the middle of the range
	assert aoc_day5.split_range((55,13),{"src_start": 58, "dst_start": 10, "map_range": 4}) == ([(55,3),(62,6)],[(10,4)])

	# Match the hole range either exactly or sarting before and finishing after the end of the range
	assert aoc_day5.split_range((55,13),{"src_start": 50, "dst_start": 10, "map_range": 20}) == ([],[(15,13)])
	assert aoc_day5.split_range((55,13),{"src_start": 55, "dst_start": 80, "map_range": 13}) == ([],[(80,13)])

    # Match at exaclty the start and end of the range
	assert aoc_day5.split_range((55,13),{"src_start": 55, "dst_start": 10, "map_range": 2}) == ([(57,11)],[(10,2)])
	assert aoc_day5.split_range((55,13),{"src_start": 66, "dst_start": 10, "map_range": 2}) == ([(55,11)],[(10,2)])

	# Match the first or the last value in the range
	assert aoc_day5.split_range((55,13),{"src_start": 53, "dst_start": 10, "map_range": 3}) == ([(56,12)],[(12,1)])
	assert aoc_day5.split_range((55,13),{"src_start": 67, "dst_start": 10, "map_range": 3}) == ([(55,12)],[(10,1)])

	# Do not match, but stop one before the start or begin one after the end of the range
	assert aoc_day5.split_range((55,13),{"src_start": 53, "dst_start": 10, "map_range": 2}) == ([(55,13)],[])
	assert aoc_day5.split_range((55,13),{"src_start": 68, "dst_start": 10, "map_range": 2}) == ([(55,13)],[])
	assert aoc_day5.split_range((55,13),{"src_start": 50, "dst_start": 10, "map_range": 5}) == ([(55,13)],[])
	assert aoc_day5.split_range((55,13),{"src_start": 68, "dst_start": 10, "map_range": 5}) == ([(55,13)],[])



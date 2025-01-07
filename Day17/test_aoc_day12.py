# Tests for Day 12

import pytest
import aoc_day17


def test_update_position():
    assert aoc_day17.update_position((0, 0), (1, 0)) == (1, 0)
    assert aoc_day17.update_position((0, 0), (0, 1)) == (0, 1)
    assert aoc_day17.update_position((0, 0), (-1, 0)) == (-1, 0)
    assert aoc_day17.update_position((0, 0), (0, -1)) == (0, -1)


def test_update_position():
    assert aoc_day17.count_previous_moves([(1, 0), (2, 0), (2, 1), (2, 2)]) == 1

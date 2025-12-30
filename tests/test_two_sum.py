"""
Tests for the Two Sum problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrays.two_sum import two_sum


def test_two_sum_basic_cases():
    """Test basic two sum functionality with valid solutions."""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


def test_two_sum_edge_cases():
    """Test edge cases for two sum."""
    # Empty array
    assert two_sum([], 5) == []
    # Single element
    assert two_sum([5], 5) == []
    # No solution
    assert two_sum([1, 2, 3], 7) == []


def test_two_sum_negative_numbers():
    """Test with negative numbers in the input."""
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]


def test_two_sum_duplicate_values():
    """Test with duplicate values."""
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]
    assert two_sum([1, 1, 1, 1], 2) == [0, 1]


def test_two_sum_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    result1 = two_sum([1, -1, 2, -2, 3], 1)
    assert set(result1) == {1, 2}  # [-1, 2] = 1
    
    result2 = two_sum([-10, 5, 5, 10], 0)
    assert set(result2) == {0, 3}  # [-10, 10] = 0

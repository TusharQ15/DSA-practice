"""
Tests for the Two Sum problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrays.two_sum import two_sum, two_sum_sorted

def test_two_sum_basic():
    """Test basic two sum functionality."""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_no_solution():
    """Test case where no two numbers sum to target."""
    assert two_sum([1, 2, 3], 7) == []

def test_two_sum_negative_numbers():
    """Test with negative numbers in the input."""
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_two_sum_sorted_basic():
    """Test two_sum_sorted with basic input."""
    assert sorted(two_sum_sorted([2, 7, 11, 15], 9)) == [2, 7]
    assert sorted(two_sum_sorted([2, 3, 4], 6)) == [2, 4]

def test_two_sum_sorted_no_solution():
    """Test two_sum_sorted with no valid solution."""
    assert two_sum_sorted([1, 2, 3], 7) == []

if __name__ == "__main__":
    pytest.main()

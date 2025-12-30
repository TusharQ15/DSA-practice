"""
Tests for the Longest Consecutive Sequence problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrays.longest_consecutive_sequence import longest_consecutive


def test_longest_consecutive_basic_cases():
    """Test basic longest consecutive sequence functionality."""
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4  # 1,2,3,4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9  # 0,1,2,3,4,5,6,7,8
    assert longest_consecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7  # -1,0,1,3,4,5,6,7,8,9


def test_longest_consecutive_edge_cases():
    """Test edge cases for longest consecutive sequence."""
    # Empty array
    assert longest_consecutive([]) == 0
    
    # Single element
    assert longest_consecutive([5]) == 1
    assert longest_consecutive([0]) == 1
    assert longest_consecutive([-1]) == 1


def test_longest_consecutive_already_sorted():
    """Test with already sorted arrays."""
    assert longest_consecutive([1, 2, 3, 4, 5]) == 5
    assert longest_consecutive([-2, -1, 0, 1]) == 4
    assert longest_consecutive([10, 11, 12, 13, 14]) == 5


def test_longest_consecutive_with_duplicates():
    """Test with duplicate elements."""
    assert longest_consecutive([1, 1, 1]) == 1
    assert longest_consecutive([2, 2, 2, 2, 2]) == 1
    assert longest_consecutive([1, 2, 2, 3, 3, 4]) == 4
    assert longest_consecutive([1, 2, 2, 3, 4, 4, 5]) == 5


def test_longest_consecutive_negative_numbers():
    """Test with negative numbers."""
    assert longest_consecutive([-1, 1, 0, 2, -2, 3]) == 6  # -2,-1,0,1,2,3
    assert longest_consecutive([-3, -1, -2, 0, 2, 1]) == 6  # -3,-2,-1,0,1,2
    assert longest_consecutive([-5, -4, -3, -2, -1]) == 5
    assert longest_consecutive([-1, -3, -5, -2, -4]) == 5


def test_longest_consecutive_disconnected_sequences():
    """Test with disconnected sequences."""
    assert longest_consecutive([10, 5, 6, 100, 101, 7]) == 3  # 5,6,7
    assert longest_consecutive([1, 3, 5, 7, 9, 11]) == 1  # All separate
    assert longest_consecutive([1, 10, 2, 20, 3, 30, 4]) == 4  # 1,2,3,4


def test_longest_consecutive_mixed_cases():
    """Test mixed positive and negative cases."""
    assert longest_consecutive([1, 2, 0, 1]) == 3  # 0,1,2
    assert longest_consecutive([1, 2, 4, 3, 5, 6, 8, 7, 9, 10]) == 10  # 1-10
    assert longest_consecutive([0, -1, 1, 2, -2, 3]) == 6  # -2,-1,0,1,2,3


def test_longest_consecutive_large_gaps():
    """Test with large gaps between numbers."""
    assert longest_consecutive([1, 100, 2, 200, 3, 300, 4]) == 4  # 1,2,3,4
    assert longest_consecutive([50, 51, 100, 101, 102, 52, 53]) == 4  # 50,51,52,53


def test_longest_consecutive_single_sequences():
    """Test cases where longest sequence is 1."""
    assert longest_consecutive([1, 3, 5, 7, 9]) == 1
    assert longest_consecutive([10, 20, 30, 40, 50]) == 1
    assert longest_consecutive([-1, -3, -5, -7]) == 1


def test_longest_consecutive_complex():
    """Test complex cases."""
    assert longest_consecutive([4, 2, 1, 6, 5]) == 2  # 1,2 or 5,6
    assert longest_consecutive([8, 6, 7, 1, 2, 3, 4]) == 4  # 1,2,3,4
    assert longest_consecutive([0, 1, 2, 5, 6, 7, 8, 9]) == 5  # 5,6,7,8,9

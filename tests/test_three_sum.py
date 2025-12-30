"""
Tests for the 3Sum problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrays.three_sum import three_sum


def test_three_sum_basic_cases():
    """Test basic three sum functionality."""
    result = three_sum([-1, 0, 1, 2, -1, -4])
    assert len(result) == 2
    assert [-1, -1, 2] in result
    assert [-1, 0, 1] in result


def test_three_sum_edge_cases():
    """Test edge cases for three sum."""
    # Empty array
    assert three_sum([]) == []
    
    # Less than 3 elements
    assert three_sum([1, 2]) == []
    assert three_sum([1]) == []
    
    # Exactly 3 elements
    assert three_sum([-1, 0, 1]) == [[-1, 0, 1]]
    assert three_sum([1, 2, 3]) == []


def test_three_sum_all_zeros():
    """Test with multiple zeros."""
    result = three_sum([0, 0, 0, 0])
    assert len(result) == 1
    assert [0, 0, 0] in result
    
    # Single zero
    assert three_sum([0]) == []
    
    # Two zeros
    assert three_sum([0, 0]) == []


def test_three_sum_no_valid_triplets():
    """Test when no valid triplets exist."""
    assert three_sum([1, 2, 3]) == []
    assert three_sum([5, 6, 7, 8]) == []
    assert three_sum([-2, 0, 1]) == []


def test_three_sum_duplicate_elements():
    """Test with duplicate elements in input."""
    result = three_sum([-1, 0, -1, 0, 1, 1])
    assert len(result) == 1
    assert [-1, 0, 1] in result


def test_three_sum_all_positive():
    """Test with all positive numbers."""
    assert three_sum([1, 2, 3, 4, 5]) == []
    assert three_sum([2, 3, 4, 5]) == []


def test_three_sum_all_negative():
    """Test with all negative numbers."""
    result = three_sum([-1, -2, -3, 4, 5, 6])
    assert len(result) == 2
    assert [-3, -2, 5] in result
    assert [-3, -1, 4] in result


def test_three_sum_mixed_large():
    """Test with larger mixed input."""
    result = three_sum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
    expected = [
        [-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], 
        [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], 
        [-1, 0, 1]
    ]
    assert len(result) == 9
    for triplet in expected:
        assert triplet in result


def test_three_sum_single_triplet():
    """Test cases that should produce exactly one triplet."""
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([-2, -1, 3]) == [[-2, -1, 3]]
    assert three_sum([-1, 2, -1]) == [[-1, -1, 2]]


def test_three_sum_early_termination():
    """Test early termination when smallest number > 0."""
    assert three_sum([1, 2, 3, 4, 5]) == []
    assert three_sum([2, 3, 4, 5, 6]) == []

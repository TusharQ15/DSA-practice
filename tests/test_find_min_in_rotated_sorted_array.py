"""
Tests for the Find Minimum in Rotated Sorted Array problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrays.find_min_in_rotated_sorted_array import find_min


def test_find_min_basic_cases():
    """Test basic find min functionality."""
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([2, 3, 4, 5, 1]) == 1


def test_find_min_no_rotation():
    """Test with non-rotated (sorted) arrays."""
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([0, 1, 2, 3, 4]) == 0
    assert find_min([1]) == 1


def test_find_min_edge_cases():
    """Test edge cases."""
    # Single element
    assert find_min([1]) == 1
    assert find_min([5]) == 5
    
    # Two elements
    assert find_min([2, 1]) == 1
    assert find_min([1, 2]) == 1


def test_find_min_various_rotations():
    """Test with different rotation amounts."""
    # Small rotation
    assert find_min([5, 1, 2, 3, 4]) == 1
    
    # Large rotation
    assert find_min([3, 4, 5, 1, 2]) == 1
    
    # Half rotation
    assert find_min([4, 5, 1, 2, 3]) == 1
    
    # Almost full rotation
    assert find_min([2, 3, 4, 5, 1]) == 1


def test_find_min_large_arrays():
    """Test with larger arrays."""
    # Large sorted array
    large_sorted = list(range(1000))
    assert find_min(large_sorted) == 0
    
    # Large rotated array
    large_rotated = list(range(500, 1000)) + list(range(500))
    assert find_min(large_rotated) == 0


def test_find_min_specific_cases():
    """Test specific known cases."""
    assert find_min([2, 3, 4, 5, 6, 7, 8, 9, 1]) == 1
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 8, 1, 2, 3]) == 1


def test_find_min_with_duplicates():
    """Test with duplicate elements (though problem specifies unique)."""
    # These should still work correctly
    assert find_min([1, 1, 1, 1]) == 1
    assert find_min([2, 2, 1, 2, 2]) == 1

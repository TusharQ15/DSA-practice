"""
Tests for the Search in Rotated Sorted Array problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrays.search_in_rotated_sorted_array import search


def test_search_in_rotated_sorted_array_basic_cases():
    """Test basic search functionality."""
    # Target present at various positions
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0


def test_search_in_rotated_sorted_array_edge_positions():
    """Test target at first, last, and pivot positions."""
    # First element
    assert search([6, 7, 0, 1, 2, 3, 4, 5], 6) == 0
    # Last element  
    assert search([4, 5, 6, 7, 0, 1, 2], 2) == 6
    # Pivot index
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_search_in_rotated_sorted_array_no_rotation():
    """Test with non-rotated (purely sorted) array."""
    assert search([0, 1, 2, 3, 4, 5, 6], 3) == 3
    assert search([0, 1, 2, 3, 4, 5, 6], 0) == 0
    assert search([0, 1, 2, 3, 4, 5, 6], 6) == 6
    assert search([0, 1, 2, 3, 4, 5, 6], 7) == -1


def test_search_in_rotated_sorted_array_small_arrays():
    """Test with small arrays."""
    # Two elements - normal
    assert search([1, 3], 1) == 0
    assert search([1, 3], 3) == 1
    assert search([1, 3], 2) == -1
    
    # Two elements - rotated
    assert search([3, 1], 3) == 0
    assert search([3, 1], 1) == 1
    assert search([3, 1], 2) == -1


def test_search_in_rotated_sorted_array_edge_cases():
    """Test edge cases."""
    # Empty array
    assert search([], 5) == -1
    
    # Single element
    assert search([5], 5) == 0
    assert search([5], 3) == -1
    
    # Target not present
    assert search([4, 5, 6, 7, 0, 1, 2], 8) == -1


def test_search_in_rotated_sorted_array_various_rotations():
    """Test with different rotation amounts."""
    # No rotation
    assert search([0, 1, 2, 3, 4, 5], 2) == 2
    
    # Small rotation
    assert search([4, 5, 0, 1, 2, 3], 0) == 2
    
    # Large rotation (almost full)
    assert search([1, 2, 3, 4, 5, 0], 0) == 5
    
    # Half rotation
    assert search([3, 4, 5, 0, 1, 2], 1) == 4

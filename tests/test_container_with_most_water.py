"""
Tests for the Container With Most Water problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrays.container_with_most_water import max_area


def test_container_with_most_water_basic_cases():
    """Test basic container with most water functionality."""
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2


def test_container_with_most_water_edge_cases():
    """Test edge cases for container with most water."""
    # Empty array
    assert max_area([]) == 0
    
    # Single element
    assert max_area([5]) == 0
    
    # Two elements
    assert max_area([1, 1]) == 1
    assert max_area([1, 2]) == 1
    assert max_area([2, 1]) == 1


def test_container_with_most_water_same_heights():
    """Test with all bars of same height."""
    assert max_area([5, 5, 5, 5, 5]) == 20
    assert max_area([3, 3, 3]) == 6
    assert max_area([1, 1, 1, 1]) == 3


def test_container_with_most_water_increasing_heights():
    """Test with strictly increasing heights."""
    assert max_area([1, 2, 3, 4, 5]) == 6
    assert max_area([1, 2, 3, 4]) == 4
    assert max_area([2, 4, 6, 8]) == 8


def test_container_with_most_water_decreasing_heights():
    """Test with strictly decreasing heights."""
    assert max_area([5, 4, 3, 2, 1]) == 6
    assert max_area([4, 3, 2, 1]) == 4
    assert max_area([8, 6, 4, 2]) == 8


def test_container_with_most_water_alternating_heights():
    """Test with alternating high and low heights."""
    assert max_area([1, 8, 1, 8, 1, 8, 1, 8, 1]) == 32
    assert max_area([2, 3, 2, 3, 2, 3]) == 9
    assert max_area([1, 10, 1, 10]) == 12


def test_container_with_most_water_zero_heights():
    """Test with zero heights."""
    assert max_area([0, 0, 0, 0]) == 0
    assert max_area([0, 5, 0, 5]) == 6
    assert max_area([5, 0, 5, 0, 5]) == 12


def test_container_with_most_water_large_values():
    """Test with large height values."""
    assert max_area([1000, 1, 1000]) == 2000
    assert max_area([100, 200, 300, 400, 500]) == 400
    assert max_area([500, 400, 300, 200, 100]) == 400


def test_container_with_most_water_specific_cases():
    """Test specific known cases."""
    assert max_area([2, 3, 4, 5, 18, 17, 6]) == 17
    assert max_area([1, 3, 2, 5, 25, 24, 5]) == 24
    assert max_area([1, 2, 4, 3]) == 4


def test_container_with_most_water_symmetric():
    """Test with symmetric patterns."""
    assert max_area([1, 2, 3, 2, 1]) == 6
    assert max_area([1, 3, 5, 3, 1]) == 8
    assert max_area([2, 4, 6, 4, 2]) == 12

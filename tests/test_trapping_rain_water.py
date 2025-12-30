"""
Tests for the Trapping Rain Water problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrays.trapping_rain_water import trap


def test_trapping_rain_water_basic_cases():
    """Test basic trapping rain water functionality."""
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([3, 0, 3]) == 3


def test_trapping_rain_water_edge_cases():
    """Test edge cases for trapping rain water."""
    # Empty array
    assert trap([]) == 0
    
    # Single bar
    assert trap([5]) == 0
    
    # Two bars
    assert trap([5, 1]) == 0
    assert trap([5, 1, 5]) == 4
    
    # Less than 3 bars
    assert trap([1]) == 0
    assert trap([1, 2]) == 0


def test_trapping_rain_water_no_water():
    """Test cases where no water can be trapped."""
    # Strictly increasing
    assert trap([1, 2, 3, 4, 5]) == 0
    
    # Strictly decreasing
    assert trap([5, 4, 3, 2, 1]) == 0
    
    # Flat surface
    assert trap([0, 0, 0, 0]) == 0
    assert trap([3, 3, 3, 3]) == 0
    
    # All zeros
    assert trap([0, 0, 0, 0, 0]) == 0


def test_trapping_rain_water_single_pit():
    """Test single valley scenarios."""
    assert trap([3, 0, 3]) == 3
    assert trap([2, 0, 2]) == 2
    assert trap([5, 1, 5]) == 4
    assert trap([4, 0, 4]) == 4


def test_trapping_rain_water_multiple_pits():
    """Test multiple valleys."""
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([2, 0, 2, 0, 2]) == 4
    assert trap([5, 2, 1, 2, 1, 5]) == 14
    assert trap([0, 2, 0, 2, 0]) == 2


def test_trapping_rain_water_complex_valleys():
    """Test complex valley patterns."""
    assert trap([2, 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 10
    assert trap([5, 4, 1, 2]) == 1
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_trapping_rain_water_plateaus():
    """Test with flat sections (plateaus)."""
    assert trap([2, 2, 0, 2, 2]) == 4
    assert trap([3, 3, 0, 3, 3]) == 6
    assert trap([4, 4, 2, 2, 4, 4]) == 8


def test_trapping_rain_water_large_heights():
    """Test with large height values."""
    assert trap([100, 0, 100]) == 100
    assert trap([50, 25, 0, 25, 50]) == 50
    assert trap([10, 5, 0, 5, 10]) == 10


def test_trapping_rain_water_uneven_edges():
    """Test with uneven left and right edges."""
    assert trap([1, 0, 2]) == 1
    assert trap([2, 0, 1]) == 1
    assert trap([5, 2, 3, 4, 1]) == 7

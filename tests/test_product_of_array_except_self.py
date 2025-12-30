"""
Tests for the Product of Array Except Self problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrays.product_of_array_except_self import product_except_self


def test_product_except_self_basic_cases():
    """Test basic product except self functionality."""
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([2, 3, 4, 5]) == [60, 40, 30, 24]
    assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]


def test_product_except_self_edge_cases():
    """Test edge cases for product except self."""
    # Empty array
    assert product_except_self([]) == []
    
    # Single element
    assert product_except_self([5]) == [1]
    
    # Two elements
    assert product_except_self([2, 3]) == [3, 2]
    assert product_except_self([1, 1]) == [1, 1]


def test_product_except_self_with_zeros():
    """Test cases with zeros."""
    # Single zero
    assert product_except_self([1, 0, 4, 2]) == [0, 8, 0, 0]
    
    # Multiple zeros
    assert product_except_self([0, 0, 1, 2]) == [0, 0, 0, 0]
    
    # Zero at start
    assert product_except_self([0, 2, 3, 4]) == [24, 0, 0, 0]
    
    # Zero at end
    assert product_except_self([1, 2, 3, 0]) == [0, 0, 0, 6]


def test_product_except_self_negative_numbers():
    """Test cases with negative numbers."""
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([-1, -2, -3, -4]) == [-24, -12, -8, -6]
    assert product_except_self([-1, 2, -3, 4]) == [-24, 12, -8, 6]


def test_product_except_self_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert product_except_self([1, -2, 3, -4]) == [24, -12, 8, -6]
    assert product_except_self([-1, 2, 3, 4]) == [24, -12, -8, -6]
    assert product_except_self([1, 2, -3, -4]) == [24, 12, -8, -6]


def test_product_except_self_large_numbers():
    """Test with large numbers."""
    assert product_except_self([100, 200, 300]) == [60000, 30000, 20000]
    assert product_except_self([10, 20, 30, 40, 50]) == [1200000, 600000, 400000, 300000, 240000]


def test_product_except_self_single_element():
    """Test single element edge case."""
    assert product_except_self([0]) == [1]
    assert product_except_self([1]) == [1]
    assert product_except_self([-5]) == [1]


def test_product_except_self_ones():
    """Test with all ones."""
    assert product_except_self([1, 1, 1]) == [1, 1, 1]
    assert product_except_self([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]


def test_product_except_self_complex():
    """Test more complex cases."""
    assert product_except_self([2, 0, 4, 1]) == [0, 8, 0, 0]
    assert product_except_self([3, 1, 2, 0]) == [0, 0, 0, 6]
    assert product_except_self([-1, 1, -1, 1]) == [-1, 1, -1, 1]

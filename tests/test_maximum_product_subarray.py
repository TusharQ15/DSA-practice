"""
Tests for the Maximum Product Subarray problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arrays.maximum_product_subarray import max_product


def test_maximum_product_subarray_basic_cases():
    """Test basic maximum product subarray functionality."""
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([-2, 0, -1]) == 0
    assert max_product([-2, 3, -4]) == 24
    assert max_product([0, 2]) == 2


def test_maximum_product_subarray_edge_cases():
    """Test edge cases for maximum product subarray."""
    # Empty array
    assert max_product([]) == 0
    
    # Single element
    assert max_product([-2]) == -2
    assert max_product([5]) == 5
    assert max_product([0]) == 0


def test_maximum_product_subarray_with_zeros():
    """Test cases with zeros."""
    assert max_product([0, 2, 0, 3]) == 3
    assert max_product([0, -2, 0, -3]) == 3
    assert max_product([1, 0, -1, 0, 2]) == 2
    assert max_product([0, 0, 0]) == 0


def test_maximum_product_subarray_negative_numbers():
    """Test cases with negative numbers."""
    assert max_product([-2, -3, -4]) == 12
    assert max_product([-1, -2, -3, -4]) == 24
    assert max_product([-2, -3, 7]) == 42
    assert max_product([-1, -3, -10, 0, 60]) == 30


def test_maximum_product_subarray_mixed_numbers():
    """Test mixed positive and negative numbers."""
    assert max_product([3, -1, 4]) == 4
    assert max_product([2, -5, -2, -4, 3]) == 24
    assert max_product([-1, 4, -4, 5]) == 80
    assert max_product([6, -3, -10, 0, 2]) == 180


def test_maximum_product_subarray_all_positive():
    """Test with all positive numbers."""
    assert max_product([1, 2, 3, 4, 5]) == 120
    assert max_product([2, 3, 4]) == 24
    assert max_product([1, 1, 1, 1]) == 1


def test_maximum_product_subarray_all_negative():
    """Test with all negative numbers."""
    assert max_product([-1, -2, -3]) == 6
    assert max_product([-2, -2]) == 4
    assert max_product([-1]) == -1
    assert max_product([-5, -4, -3, -2, -1]) == 120


def test_maximum_product_subarray_single_negative():
    """Test with single negative number."""
    assert max_product([-2]) == -2
    assert max_product([-10]) == -10
    assert max_product([-1]) == -1


def test_maximum_product_subarray_complex_cases():
    """Test complex cases."""
    assert max_product([2, -5, -2, -4, 3]) == 24
    assert max_product([-2, -3, 0, -2, -40]) == 80
    assert max_product([7, -2, -4]) == 56
    assert max_product([-2, -3, 7, -5, -4, 2, -1, -1, -3, -5]) == 1088640


def test_maximum_product_subarray_with_one():
    """Test cases involving the number 1."""
    assert max_product([1, -2, -3, 0, 1, -1]) == 6
    assert max_product([1, 1, 1, -1, 1]) == 1
    assert max_product([-1, 1, -1, 1, -1]) == 1

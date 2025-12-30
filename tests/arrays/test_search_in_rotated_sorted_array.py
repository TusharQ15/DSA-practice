import pytest

from arrays.search_in_rotated_sorted_array import search


def test_basic_case():
    """Test basic rotated array case from problem statement."""
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_target_not_found():
    """Test when target is not present in the array."""
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_empty_array():
    """Test edge case with empty array."""
    assert search([], 1) == -1


def test_single_element_found():
    """Test single element array where target is found."""
    assert search([1], 1) == 0


def test_single_element_not_found():
    """Test single element array where target is not found."""
    assert search([1], 0) == -1


def test_target_first_element():
    """Test when target is the first element."""
    assert search([4, 5, 6, 7, 0, 1, 2], 4) == 0


def test_target_last_element():
    """Test when target is the last element."""
    assert search([4, 5, 6, 7, 0, 1, 2], 2) == 6


def test_no_rotation():
    """Test array that is not rotated (regular sorted array)."""
    assert search([1, 2, 3, 4, 5], 3) == 2


def test_max_rotation():
    """Test array rotated by maximum amount (length-1)."""
    assert search([2, 3, 4, 5, 1], 1) == 4


def test_large_array():
    """Test with larger rotated array."""
    nums = list(range(10, 50)) + list(range(0, 10))
    assert search(nums, 25) == 15
    assert search(nums, 5) == 45


def test_negative_numbers():
    """Test with negative numbers in rotated array."""
    assert search([-3, -2, -1, 0, 1, 2, 3], 0) == 3
    assert search([1, 2, 3, -3, -2, -1, 0], -2) == 4

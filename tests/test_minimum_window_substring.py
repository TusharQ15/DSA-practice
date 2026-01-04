import pytest
from strings.minimum_window_substring import min_window


def test_typical_valid_window():
    """Test typical case where a valid window exists."""
    s = "ADOBECODEBANC"
    t = "ABC"
    result = min_window(s, t)
    assert result == "BANC"


def test_no_valid_window():
    """Test case where no valid window exists."""
    s = "HELLO"
    t = "XYZ"
    result = min_window(s, t)
    assert result == ""


def test_s_equals_t():
    """Test case where s == t."""
    s = "ABC"
    t = "ABC"
    result = min_window(s, t)
    assert result == "ABC"


def test_repeated_characters_in_t():
    """Test case with repeated characters in t."""
    s = "AAABBBCCC"
    t = "AAB"
    result = min_window(s, t)
    assert result == "AAB"


def test_very_small_strings():
    """Test case with very small strings (length 1-2)."""
    s = "a"
    t = "a"
    result = min_window(s, t)
    assert result == "a"
    
    s = "ab"
    t = "b"
    result = min_window(s, t)
    assert result == "b"


def test_empty_strings():
    """Test case with empty strings."""
    assert min_window("", "ABC") == ""
    assert min_window("ABC", "") == ""
    assert min_window("", "") == ""


def test_t_longer_than_s():
    """Test case where t is longer than s."""
    s = "AB"
    t = "ABC"
    result = min_window(s, t)
    assert result == ""


def test_multiple_possible_windows():
    """Test case with multiple possible windows, should return smallest."""
    s = "BACDEBAC"
    t = "ABC"
    result = min_window(s, t)
    # Both "BAC" and "CAB" are valid, but "BAC" appears first
    assert result == "BAC"


def test_characters_not_in_order():
    """Test case where required characters are not in order."""
    s = "XYZABCXYZ"
    t = "CBA"
    result = min_window(s, t)
    assert result == "ABC"


def test_duplicate_characters_window():
    """Test case with duplicate characters in the window."""
    s = "AAABAAABA"
    t = "AAB"
    result = min_window(s, t)
    assert result == "AAB"

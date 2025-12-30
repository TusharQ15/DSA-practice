import pytest
from strings.valid_anagram import is_anagram

def test_valid_anagram_typical_true():
    """Test typical true anagram case."""
    assert is_anagram("anagram", "nagaram") == True

def test_valid_anagram_typical_false():
    """Test typical false case with one different character."""
    assert is_anagram("rat", "car") == False

def test_valid_anagram_different_lengths():
    """Test case with different lengths."""
    assert is_anagram("a", "aa") == False
    assert is_anagram("abc", "ab") == False

def test_valid_anagram_repeated_chars_false():
    """Test strings with repeated characters that are not anagrams."""
    assert is_anagram("aacc", "ccac") == False

def test_valid_anagram_repeated_chars_true():
    """Test strings with repeated characters that are anagrams."""
    assert is_anagram("abbb", "bbab") == True

def test_valid_anagram_empty_strings():
    """Test empty strings edge case."""
    assert is_anagram("", "") == True

def test_valid_anagram_single_char():
    """Test single character strings."""
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "b") == False

def test_valid_anagram_case_sensitivity():
    """Test case sensitivity."""
    assert is_anagram("A", "a") == False
    assert is_anagram("Abc", "cba") == False

def test_valid_anagram_unicode():
    """Test with Unicode characters."""
    assert is_anagram("café", "éfac") == True

def test_valid_anagram_with_spaces():
    """Test with spaces (should be treated as characters)."""
    assert is_anagram("a b", "b a") == True
    assert is_anagram("ab", "a b") == False

def test_valid_anagram_long_strings():
    """Test with longer strings to ensure efficiency."""
    s = "a" * 1000 + "b" * 1000
    t = "b" * 1000 + "a" * 1000
    assert is_anagram(s, t) == True

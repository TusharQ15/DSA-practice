"""
Tests for the Valid Anagram problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strings.valid_anagram import is_anagram


def test_valid_anagram_basic_cases():
    """Test basic anagram cases."""
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("listen", "silent") == True


def test_valid_anagram_edge_cases():
    """Test edge cases for anagram."""
    # Empty strings
    assert is_anagram("", "") == True
    
    # Empty vs non-empty
    assert is_anagram("", "a") == False
    assert is_anagram("a", "") == False
    
    # Single character
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "b") == False


def test_valid_anagram_different_lengths():
    """Test cases with different lengths."""
    assert is_anagram("a", "aa") == False
    assert is_anagram("ab", "a") == False
    assert is_anagram("abc", "ab") == False
    assert is_anagram("", "a") == False


def test_valid_anagram_repeated_characters():
    """Test cases with repeated characters."""
    assert is_anagram("aabbcc", "abcabc") == True
    assert is_anagram("aabbcc", "abccba") == True
    assert is_anagram("aaabbb", "ab") == False
    assert is_anagram("aabbcc", "abbccd") == False


def test_valid_anagram_case_sensitive():
    """Test case sensitivity."""
    assert is_anagram("Hello", "hello") == False
    assert is_anagram("Hello", "olleH") == True
    assert is_anagram("AbC", "Cba") == False
    assert is_anagram("AbC", "CbA") == True


def test_valid_anagram_unicode():
    """Test with Unicode characters."""
    assert is_anagram("café", "éfac") == True
    assert is_anagram("ñandú", "úñand") == True
    assert is_anagram("café", "cafe") == False  # Missing accent
    assert is_anagram("こんにちは", "はこんにち") == True  # Japanese


def test_valid_anagram_numbers_and_symbols():
    """Test with numbers and symbols."""
    assert is_anagram("123", "321") == True
    assert is_anagram("a1b2", "2b1a") == True
    assert is_anagram("hello!", "!olleh") == True
    assert is_anagram("test123", "test321") == False


def test_valid_anagram_long_strings():
    """Test with longer strings."""
    long_str1 = "a" * 1000 + "b" * 1000
    long_str2 = "b" * 1000 + "a" * 1000
    assert is_anagram(long_str1, long_str2) == True
    
    long_str3 = "a" * 999 + "b" * 1000
    assert is_anagram(long_str1, long_str3) == False


def test_valid_anagram_mixed_content():
    """Test with mixed alphanumeric and special characters."""
    assert is_anagram("a1b2c3!", "!3c2b1a") == True
    assert is_anagram("hello-world", "world-hello") == True
    assert is_anagram("test_case", "case-test") == True
    assert is_anagram("test_case", "testcase") == False

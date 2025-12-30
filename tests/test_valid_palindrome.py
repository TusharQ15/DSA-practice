"""
Tests for the Valid Palindrome problem solution.
"""
import pytest
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from strings.is_palindrome import is_palindrome


def test_valid_palindrome_basic_cases():
    """Test basic palindrome cases."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("aba") == True


def test_valid_palindrome_edge_cases():
    """Test edge cases for palindrome."""
    # Empty string
    assert is_palindrome("") == True
    
    # Single character
    assert is_palindrome("a") == True
    
    # Only non-alphanumeric characters
    assert is_palindrome("!!!") == True
    assert is_palindrome("   ") == True
    assert is_palindrome("@#$%^&*()") == True


def test_valid_palindrome_case_insensitive():
    """Test case insensitive behavior."""
    assert is_palindrome("Madam") == True
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("NoLemonNoMelon") == True


def test_valid_palindrome_mixed_alphanumeric():
    """Test mixed alphanumeric cases."""
    assert is_palindrome("0P") == False
    assert is_palindrome("12321") == True
    assert is_palindrome("1a2b2a1") == True
    assert is_palindrome("12321 A man, a plan, a canal: Panama 12321") == True


def test_valid_palindrome_unicode():
    """Test with Unicode characters."""
    # Note: isalnum() works with Unicode, so these should work correctly
    assert is_palindrome("ññ") == True  # Same Unicode characters
    assert is_palindrome("ñN") == False  # Different case but same letter
    assert is_palindrome("cafééfac") == True  # With accents


def test_valid_palindrome_numeric():
    """Test numeric palindromes."""
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False
    assert is_palindrome("1") == True
    assert is_palindrome("11") == True


def test_valid_palindrome_with_spaces_and_punctuation():
    """Test strings with spaces and punctuation."""
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("Eva, can I see bees in a cave?") == True

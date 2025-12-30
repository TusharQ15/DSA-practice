import pytest
from strings.is_palindrome import is_palindrome

def test_valid_palindrome_example():
    """Test example with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_valid_palindrome_non_palindrome():
    """Test non-palindrome with spaces."""
    assert is_palindrome("race a car") == False

def test_valid_palindrome_only_non_alphanumeric():
    """Test string with only non-alphanumeric characters."""
    assert is_palindrome("!!!") == True

def test_valid_palindrome_single_character():
    """Test single character."""
    assert is_palindrome("a") == True

def test_valid_palindrome_mixed_alphanumeric():
    """Test mixed alphanumeric case."""
    assert is_palindrome("0P") == False

def test_valid_palindrome_empty_string():
    """Test empty string behavior."""
    assert is_palindrome("") == True

def test_valid_palindrome_numeric():
    """Test numeric palindrome."""
    assert is_palindrome("12321") == True

def test_valid_palindrome_case_insensitive():
    """Test case insensitive behavior."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("Madam") == True

def test_valid_palindrome_with_spaces():
    """Test string with spaces only."""
    assert is_palindrome("   ") == True

def test_valid_palindrome_mixed_case_and_punctuation():
    """Test mixed case with punctuation."""
    assert is_palindrome("No 'x' in Nixon") == True

def test_valid_palindrome_mixed_alphanumeric_palindrome():
    """Test mixed alphanumeric palindrome."""
    assert is_palindrome("12321 A man, a plan, a canal: Panama 12321") == True
    assert is_palindrome("1a2b2a1") == True

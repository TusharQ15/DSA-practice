"""
Tests for longest substring without repeating characters problem
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strings.longest_substring_without_repeating_characters import length_of_longest_substring

def test_longest_substring_basic():
    """Test basic cases"""
    # Test case 1: "abcabcbb" → 3 ("abc")
    assert length_of_longest_substring("abcabcbb") == 3
    
    # Test case 2: "bbbbb" → 1 ("b")
    assert length_of_longest_substring("bbbbb") == 1
    
    # Test case 3: "pwwkew" → 3 ("wke")
    assert length_of_longest_substring("pwwkew") == 3

def test_longest_substring_edge_cases():
    """Test edge cases"""
    # Test case 4: Empty string → 0
    assert length_of_longest_substring("") == 0
    
    # Test case 5: "dvdf" → 3 ("vdf")
    assert length_of_longest_substring("dvdf") == 3
    
    # Test case 6: All unique characters → full length
    assert length_of_longest_substring("abcdef") == 6

def test_longest_substring_single_character():
    """Test single character cases"""
    assert length_of_longest_substring("a") == 1
    assert length_of_longest_substring("aaaaa") == 1

def test_longest_substring_mixed_patterns():
    """Test mixed patterns"""
    # Test with spaces
    assert length_of_longest_substring("abc def gh") == 7  # "c def g"
    
    # Test with numbers and letters
    assert length_of_longest_substring("a1b2c3d4e5") == 10
    
    # Test with repeated pattern
    assert length_of_longest_substring("abcaefgh") == 7  # "bcaefgh"

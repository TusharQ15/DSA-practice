"""
Tests for longest repeating character replacement problem
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strings.longest_repeating_character_replacement import character_replacement

def test_character_replacement_basic():
    """Test basic cases"""
    # Test case 1: "ABAB" → 2 (k=0)
    assert character_replacement("ABAB", 0) == 2
    
    # Test case 2: "AABABBA" → 5 (k=1)
    assert character_replacement("AABABBA", 1) == 5
    
    # Test case 3: "ABBABBBA" → 8 (k=2)
    assert character_replacement("ABBABBBA", 2) == 8

def test_character_replacement_edge_cases():
    """Test edge cases"""
    # Test case 4: "AAAA" → 4 (k=0)
    assert character_replacement("AAAA", 0) == 4
    
    # Test case 5: "ABBB" → 4 (k=2)
    assert character_replacement("ABBB", 2) == 4
    
    # Test case 6: Empty string → 0
    assert character_replacement("", 5) == 0

def test_character_replacement_large_k():
    """Test cases with large k values"""
    # Test case 7: k larger than string length
    assert character_replacement("ABC", 10) == 3
    
    # Test case 8: All same characters with any k
    assert character_replacement("AAAAAA", 3) == 6
    assert character_replacement("BBBBBB", 0) == 6

def test_character_replacement_mixed_patterns():
    """Test mixed patterns"""
    # Test case 9: Alternating pattern
    assert character_replacement("ABABABAB", 3) == 8
    
    # Test case 10: Long string with one dominant character
    assert character_replacement("AAABBBBB", 1) == 6

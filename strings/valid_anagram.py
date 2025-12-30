"""
Problem: Valid Anagram

Source: https://leetcode.com/problems/valid-anagram/

Difficulty: Easy

Approach: Hash map frequency count with early exit on mismatch

Time Complexity: O(n)

Space Complexity: O(1) for ASCII, O(n) for Unicode
"""

from typing import Dict


def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    Args:
        s: First string (may contain any Unicode characters)
        t: Second string (may contain any Unicode characters)
        
    Returns:
        True if t is an anagram of s, False otherwise.
        
    Edge Cases:
        - Different lengths immediately return False
        - Empty strings return True
        - Case is considered (case-sensitive)
        - All Unicode characters are supported
        - Works with duplicate characters
    """
    # Early exit if lengths differ
    if len(s) != len(t):
        return False
    
    # Use a dictionary to count character frequencies
    char_counts: Dict[str, int] = {}
    
    # Count characters in s
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Subtract counts using characters in t
    for char in t:
        if char not in char_counts:
            return False
        char_counts[char] -= 1
        if char_counts[char] < 0:
            return False
    
    # All counts should be zero
    return True

"""
Problem: Valid Anagram
Source: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy

Approach: Use a hash map to count character frequencies in the first string,
then decrement counts for the second string and early-exit on mismatch.
Time Complexity: O(n)
Space Complexity: O(n) - hash map for character frequencies
"""

from typing import Dict

def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    Args:
        s (str): First string
        t (str): Second string
        
    Returns:
        bool: True if t is an anagram of s, False otherwise
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

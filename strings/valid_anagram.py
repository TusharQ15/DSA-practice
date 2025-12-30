"""
Problem: Valid Anagram

Source: https://leetcode.com/problems/valid-anagram/

Difficulty: Easy

Approach: character frequency counting using a hash map; compare counts for both strings; early-exit if lengths differ.

Time Complexity: O(n)

Space Complexity: O(1) - using fixed-size array for lowercase letters, or O(n) for general Unicode
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

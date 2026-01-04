"""
Problem: Longest Substring Without Repeating Characters

Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Difficulty: Medium

Approach: 
Sliding window with hash map tracking last seen index of each character. 
Expand right pointer, if duplicate found move left to max(left, last_seen[char]+1).
Track max length seen so far.

Time Complexity: O(n)
Space Complexity: O(min(n, charset))
"""

from typing import Dict

def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring with all unique characters
        
    Edge Cases:
        - Empty string returns 0
        - String with all unique characters returns len(s)
        - String with all same characters returns 1
    """
    char_to_index: Dict[str, int] = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If character seen before and is within current window
        if char in char_to_index and char_to_index[char] >= left:
            # Move left pointer to position after the previous occurrence
            left = char_to_index[char] + 1
        
        # Update the last seen index of current character
        char_to_index[char] = right
        
        # Update max length with current window size
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    
    return max_length

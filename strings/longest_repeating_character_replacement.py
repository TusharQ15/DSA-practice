"""
Problem: Longest Repeating Character Replacement

Source: https://leetcode.com/problems/longest-repeating-character-replacement/

Difficulty: Medium

Approach: 
Sliding window where (window_length - max_frequency) <= k
Track character frequencies in window using hash map/array
Shrink window from left when condition violated

Time Complexity: O(n)
Space Complexity: O(1) - fixed size array for 26 uppercase letters
"""

from typing import List

def character_replacement(s: str, k: int) -> int:
    """
    Find the length of the longest substring containing the same letter after
    performing at most k character replacements.
    
    Args:
        s: Input string consisting of uppercase English letters (A-Z)
        k: Maximum number of character replacements allowed (k >= 0)
        
    Returns:
        Length of the longest possible substring after at most k replacements
        
    Edge Cases:
        - Empty string returns 0
        - k >= len(s) returns len(s)
        - All characters already the same returns len(s)
        
    Note: Function assumes input contains only uppercase English letters.
    For lowercase or mixed case, convert to uppercase before calling.
    """
    char_counts: List[int] = [0] * 26  # For uppercase English letters
    left = 0
    max_length = 0
    max_frequency = 0
    
    for right, char in enumerate(s):
        # Update frequency count for current character
        char_index = ord(char) - ord('A')
        char_counts[char_index] += 1
        
        # Update max frequency in current window
        max_frequency = max(max_frequency, char_counts[char_index])
        
        # Current window length
        window_length = right - left + 1
        
        # If we need more than k replacements, shrink window from left
        if window_length - max_frequency > k:
            left_char_index = ord(s[left]) - ord('A')
            char_counts[left_char_index] -= 1
            left += 1
            # Recalculate max_frequency when shrinking window
            max_frequency = max(char_counts)
        
        # Update max length
        max_length = max(max_length, window_length)
    
    return max_length

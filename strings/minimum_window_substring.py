"""
Problem: Minimum Window Substring

Source: https://leetcode.com/problems/minimum-window-substring/

Difficulty: Hard

Approach:
- Use a sliding window with two pointers [left, right] over s while tracking counts of required characters from t.
- Maintain a hash map of required counts and another for current window; shrink from the left when window is valid to find the minimum.
- Track when window contains all required characters and minimize window size.

Time Complexity: O(n + m) where n is length of s, m is length of t
Space Complexity: O(k) where k is number of unique characters in t
"""

from typing import Dict
from collections import Counter


def min_window(s: str, t: str) -> str:
    """
    Find the minimum window substring of s containing all characters of t.
    
    Args:
        s: Source string to search in
        t: Target string with required characters
        
    Returns:
        The minimum window substring, or empty string if no such window exists
        
    Example:
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
    """
    if not s or not t or len(t) > len(s):
        return ""
    
    # Count required characters
    need = Counter(t)
    have = {}
    required = len(need)  # Number of unique characters needed
    formed = 0  # Number of unique characters with required count in current window
    
    left = 0
    min_len = float('inf')
    min_window = ""
    
    # Expand window with right pointer
    for right, char in enumerate(s):
        # Add current character to window
        have[char] = have.get(char, 0) + 1
        
        # Check if current character meets required count
        if char in need and have[char] == need[char]:
            formed += 1
        
        # When window is valid, try to shrink from left
        while formed == required and left <= right:
            # Update minimum window if smaller
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_window = s[left:right + 1]
            
            # Remove leftmost character and move left pointer
            left_char = s[left]
            have[left_char] -= 1
            
            # Check if window is no longer valid
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            
            left += 1
    
    return min_window

"""
Problem: Valid Palindrome

Source: https://leetcode.com/problems/valid-palindrome/

Difficulty: Easy

Approach: Two pointers from both ends, skipping non-alphanumeric characters

Time Complexity: O(n)

Space Complexity: O(1)
"""

from typing import List


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, considering only alphanumeric characters and ignoring case.
    
    Args:
        s: Input string to check (may contain any Unicode characters)
        
    Returns:
        True if the string is a palindrome under the specified conditions, False otherwise.
        
    Edge Cases:
        - Empty string returns True
        - String with only non-alphanumeric characters returns True
        - Single character returns True
        - Case is ignored for comparison
        - Only alphanumeric characters are considered
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
            
        # Compare lowercase characters
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

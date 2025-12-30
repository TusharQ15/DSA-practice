"""
Problem: Valid Palindrome

Source: https://leetcode.com/problems/valid-palindrome/

Difficulty: Easy

Approach: two-pointer technique from both ends, skipping non-alphanumeric characters and comparing lowercase characters.

Time Complexity: O(n)

Space Complexity: O(1)
"""

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, considering only alphanumeric characters and ignoring case.
    
    Args:
        s (str): Input string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
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

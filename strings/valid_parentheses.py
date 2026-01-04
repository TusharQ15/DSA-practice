"""
Problem: Valid Parentheses
Source: https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy

Approach:
- Use stack to track opening brackets; pop and match closing brackets.
- Map closing brackets to their opening counterparts for quick lookup.
- Return False if stack empty when closing bracket encountered.
- Empty stack at end means perfectly balanced.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def is_valid_parentheses(s: str) -> bool:
    """
    Check if a string containing parentheses, brackets, and braces is valid.
    
    Args:
        s: Input string containing only '()[]{}' characters
        
    Returns:
        True if the string is valid (all brackets are properly closed and nested),
        False otherwise.
        
    Edge Cases:
        - Empty string returns True
        - Single opening bracket returns False
        - Mismatched closing bracket returns False
        - Properly nested brackets return True
    """
    # Stack to store opening brackets
    stack = []
    
    # Mapping of closing brackets to their opening counterparts
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map.values():  # Opening bracket
            stack.append(char)
        elif char in bracket_map:  # Closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            # Invalid character (shouldn't happen per problem constraints)
            return False
    
    # Valid if stack is empty (all brackets matched)
    return len(stack) == 0

"""
Problem: Generate Parentheses
Source: https://leetcode.com/problems/generate-parentheses/
Difficulty: Medium

Approach:
- Use backtracking to build valid combinations recursively.
- Add '(' if open count < n; add ')' if close count < open count.
- Base case: when open == close == n, add to result.
- Generates only valid combinations by construction.

Time Complexity: O(4^n / sqrt(n)) - Catalan number approximation
Space Complexity: O(n) for recursion stack + O(4^n / sqrt(n)) for result
"""

from typing import List


def generate_parentheses(n: int) -> List[str]:
    """
    Generate all combinations of well-formed parentheses for n pairs.
    
    Args:
        n: Number of pairs of parentheses
        
    Returns:
        List of all valid parentheses combinations.
        
    Edge Cases:
        - n = 0 returns empty list
        - n = 1 returns ["()"]
        - Results are in lexicographic order due to backtracking approach
    """
    if n == 0:
        return []
    
    result = []
    
    def backtrack(current: str, open_count: int, close_count: int) -> None:
        """
        Recursive helper to build valid parentheses combinations.
        
        Args:
            current: Current string being built
            open_count: Number of '(' used so far
            close_count: Number of ')' used so far
        """
        # Base case: complete combination
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Add opening parenthesis if we haven't used all n
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        
        # Add closing parenthesis if it won't make the string invalid
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    # Start with empty string
    backtrack('', 0, 0)
    return result

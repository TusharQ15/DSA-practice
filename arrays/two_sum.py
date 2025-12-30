"""
Problem: Two Sum

Source: https://leetcode.com/problems/two-sum/

Difficulty: Easy

Approach: Hash map to store complement lookup while iterating once through array

Time Complexity: O(n)

Space Complexity: O(n)
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers that add up to target.
    
    Args:
        nums: List of integers (may contain duplicates)
        target: Target sum
        
    Returns:
        List of two indices whose values sum to target, or empty list if no solution.
        Returns indices in the order they appear in the array.
        
    Edge Cases:
        - Empty array returns empty list
        - Array with one element returns empty list
        - Multiple solutions: returns first found pair
        - Negative numbers are handled correctly
        - Duplicate values are handled correctly
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

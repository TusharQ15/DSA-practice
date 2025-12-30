"""
Problem: Maximum Subarray

Source: https://leetcode.com/problems/maximum-subarray/

Difficulty: Medium

Approach: Kadane's algorithm to track current and maximum subarray sum

Time Complexity: O(n)

Space Complexity: O(1)
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    Find the contiguous subarray with the largest sum.
    
    Args:
        nums: List of integers (can be positive, negative, or zero)
        
    Returns:
        Maximum sum of any contiguous subarray.
        
    Edge Cases:
        - Empty array returns 0
        - Single element returns that element
        - All negative numbers returns the least negative number
        - All positive numbers returns sum of all elements
    """
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        # Choose between extending previous subarray or starting new subarray
        current_sum = max(num, current_sum + num)
        # Update max_sum if current subarray sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum

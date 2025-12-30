"""
Problem: Maximum Product Subarray

Source: https://leetcode.com/problems/maximum-product-subarray/

Difficulty: Medium

Approach: Dynamic programming tracking both max and min products to handle negative numbers

Time Complexity: O(n)

Space Complexity: O(1)
"""

from typing import List


def max_product(nums: List[int]) -> int:
    """
    Find the contiguous subarray with the largest product.
    
    Args:
        nums: List of integers (can be positive, negative, or zero)
        
    Returns:
        Maximum product of any contiguous subarray.
        
    Edge Cases:
        - Empty array returns 0
        - Single element returns that element
        - Contains zeros resets the product
        - Negative numbers can flip min to max
        - All negative numbers handled correctly
    """
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod  # Swap when negative
        
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        
        result = max(result, max_prod)
    
    return result

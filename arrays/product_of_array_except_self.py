"""
Problem: Product of Array Except Self

Source: https://leetcode.com/problems/product-of-array-except-self/

Difficulty: Medium

Approach: Two-pass solution with prefix and suffix products

Time Complexity: O(n)

Space Complexity: O(1) excluding output
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    """
    Return an array where each element is the product of all other elements.
    
    Args:
        nums: List of integers (can be positive, negative, or zero)
        
    Returns:
        Array where result[i] is the product of all elements except nums[i].
        
    Edge Cases:
        - Empty array returns empty array
        - Single element returns [1]
        - Zeros handled correctly (only position with zero gets product of others)
        - Negative numbers handled correctly
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate prefix products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Calculate suffix products and multiply with prefix
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

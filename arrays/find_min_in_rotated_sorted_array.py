"""
Problem: Find Minimum in Rotated Sorted Array

Source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Difficulty: Medium

Approach: Binary search comparing middle element with rightmost to find pivot

Time Complexity: O(log n)

Space Complexity: O(1)
"""

from typing import List


def find_min(nums: List[int]) -> int:
    """
    Find the minimum element in a rotated sorted array.
    
    Args:
        nums: List of unique integers sorted in ascending order and rotated at some pivot
        
    Returns:
        The minimum element in the array.
        
    Edge Cases:
        - Empty array behavior undefined (LeetCode guarantees non-empty)
        - Single element returns that element
        - Not rotated (sorted) returns first element
        - Fully rotated returns smallest element
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element is greater than right element, search right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Else search left half including mid
            right = mid
            
    return nums[left]

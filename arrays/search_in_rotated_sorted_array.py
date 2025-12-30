"""
Problem: Search in Rotated Sorted Array

Source: https://leetcode.com/problems/search-in-rotated-sorted-array/

Difficulty: Medium

Approach: Modified binary search to handle rotation by determining which half is sorted at each step

Time Complexity: O(log n)

Space Complexity: O(1)
"""

from __future__ import annotations
from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Search for target in a rotated sorted array.
    
    Args:
        nums: List of unique integers sorted in ascending order and rotated at some pivot
        target: The integer to search for
              
    Returns:
        The index of target if it is in nums, or -1 if not found.
        
    Edge Cases:
        - Empty array returns -1
        - Single element array works correctly
        - Array not rotated (purely sorted) works correctly
        - Target not present returns -1
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
            
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

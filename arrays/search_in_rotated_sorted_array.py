"""
Search in Rotated Sorted Array - Binary Search in Rotated Array

Problem link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Topics: Array, Binary Search
Difficulty: Medium

Approach:

- Use modified binary search to handle rotation
- Determine which half is sorted at each step
- Check if target lies in the sorted half
- Search in the appropriate half based on comparison
- Continue until target found or search space exhausted

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from __future__ import annotations
from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Search for target in a rotated sorted array.
    
    Args:
        nums: List of unique integers sorted in ascending order and
              rotated at some pivot (e.g., [4,5,6,7,0,1,2])
        target: The integer to search for
              
    Returns:
        The index of target if it is in nums, or -1 if not found.
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

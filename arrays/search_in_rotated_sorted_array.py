"""
Problem: Search in Rotated Sorted Array
Source: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: Medium

Approach:
1. Use binary search to find the pivot point where rotation occurs
2. Determine which half of the array is sorted
3. Check if target lies within the sorted half, otherwise search the other half
4. Perform regular binary search on the appropriate half
"""
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


# Test cases
import unittest


class TestSearchInRotatedArray(unittest.TestCase):
    def test_search_rotated(self):
        # Test case 1: Target in right half
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 0), 4)
        
        # Test case 2: Target not in array
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 3), -1)
        
        # Test case 3: Single element array (target found)
        self.assertEqual(search([1], 1), 0)
        
        # Test case 4: Single element array (target not found)
        self.assertEqual(search([1], 0), -1)
        
        # Test case 5: Target is first element
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 4), 0)
        
        # Test case 6: Target is last element
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 2), 6)
        
        # Test case 7: Array not rotated
        self.assertEqual(search([1, 2, 3, 4, 5], 3), 2)


if __name__ == "__main__":
    unittest.main()

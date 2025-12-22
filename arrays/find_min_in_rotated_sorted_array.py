"""
Problem: Find Minimum in Rotated Sorted Array
Source: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: Medium

Approach:
We use binary search to find the pivot point where the rotation occurs.
The minimum element is at the pivot point. We compare the middle element
with the rightmost element to determine which half to search in.
"""
from typing import List


def find_min(nums: List[int]) -> int:
    """
    Find the minimum element in a rotated sorted array.
    
    Args:
        nums: List of unique integers sorted in ascending order and
              rotated at some pivot (e.g., [3,4,5,1,2])
              
    Returns:
        The minimum element in the array.
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


# Test cases
import unittest


class TestFindMin(unittest.TestCase):
    def test_find_min(self):
        # Test case 1: Normal rotation
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)
        
        # Test case 2: Already sorted array (no rotation)
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
        
        # Test case 3: Single element
        self.assertEqual(find_min([1]), 1)
        
        # Test case 4: Two elements
        self.assertEqual(find_min([2, 1]), 1)
        
        # Test case 5: Rotated at last element
        self.assertEqual(find_min([2, 3, 4, 5, 1]), 1)
        
        # Test case 6: All elements same (though problem says unique elements)
        self.assertEqual(find_min([1, 1, 1, 1]), 1)


if __name__ == "__main__":
    unittest.main()

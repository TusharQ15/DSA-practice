"""
Problem: Maximum Subarray
Source: https://leetcode.com/problems/maximum-subarray/
Difficulty: Medium

Approach:
1. Use Kadane's algorithm to find the maximum sum subarray
2. Keep track of current sum and maximum sum found so far
3. Reset current sum if it becomes negative

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(1) - Constant extra space used
"""
from typing import List

def max_subarray(nums: List[int]) -> int:
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        # Choose between extending previous subarray or starting new subarray
        current_sum = max(num, current_sum + num)
        # Update max_sum if current subarray sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum


import unittest

class TestMaxSubarray(unittest.TestCase):
    def test_example_1(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray(nums), 6)  # [4, -1, 2, 1]
    
    def test_all_negative(self):
        nums = [-2, -1, -3, -4]
        self.assertEqual(max_subarray(nums), -1)  # [-1]
    
    def test_single_element(self):
        nums = [5]
        self.assertEqual(max_subarray(nums), 5)
    
    def test_mixed_positive_negative(self):
        nums = [1, -2, 3, 10, -4, 7, 2, -5]
        self.assertEqual(max_subarray(nums), 18)  # [3, 10, -4, 7, 2]
    
    def test_all_positive(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(max_subarray(nums), 15)  # [1, 2, 3, 4, 5]
    
    def test_with_zero(self):
        nums = [0, -1, 2, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray(nums), 6)  # [4, -1, 2, 1]


if __name__ == "__main__":
    unittest.main()

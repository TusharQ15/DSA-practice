"""
Problem: Trapping Rain Water
Source: https://leetcode.com/problems/trapping-rain-water/
Difficulty: Hard

Approach:
The solution uses two pointers to track the maximum height from left and right.
At each step, the amount of water that can be trapped is determined by the minimum
of the left and right maximums minus the current height. We move the pointer with
the smaller maximum height towards the center, updating the maximum heights as we go.

Time Complexity: O(n)
Space Complexity: O(1)
"""
from typing import List


def trap(height: List[int]) -> int:
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water


import unittest


class TestTrappingRainWater(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
    
    def test_all_zeros(self):
        self.assertEqual(trap([0, 0, 0, 0]), 0)
    
    def test_increasing_heights(self):
        self.assertEqual(trap([1, 2, 3, 4, 5]), 0)
    
    def test_decreasing_heights(self):
        self.assertEqual(trap([5, 4, 3, 2, 1]), 0)
    
    def test_single_and_two_bars(self):
        self.assertEqual(trap([5]), 0)
        self.assertEqual(trap([5, 8]), 0)
    
    def test_complex_valley(self):
        self.assertEqual(trap([2, 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 10)


if __name__ == "__main__":
    unittest.main()

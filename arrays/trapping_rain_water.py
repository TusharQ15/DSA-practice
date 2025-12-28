"""
Problem: Trapping Rain Water

Source: https://leetcode.com/problems/trapping-rain-water/

Difficulty: Hard

Approach:
- Use two pointers starting from both ends of the array.
- Track max heights from the left and right.
- At each step, move the pointer with the smaller current height.
- For that side, if the current height is less than the max for that side,
  the difference contributes to trapped water.
- This works because the water level on a side is limited by the smaller
  of the two max heights seen so far.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def trap(height: List[int]) -> int:
    """
    Calculate how much water can be trapped after raining.

    Args:
        height: List of non-negative integers representing elevation map.

    Returns:
        Total amount of water that can be trapped.
    """
    if not height or len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max = 0
    right_max = 0
    water = 0

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

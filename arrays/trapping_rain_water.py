"""
Problem: Trapping Rain Water

Source: https://leetcode.com/problems/trapping-rain-water/

Difficulty: Hard

Approach:
Use two pointers (left, right) to track the maximum height to the left and right of each position.
At each step, move the pointer pointing to the smaller height, because the water trapped at that side
is limited by the smaller boundary. Maintain left_max and right_max and accumulate trapped water as:
- If height[left] < height[right]:
    - If height[left] >= left_max: update left_max
    - Else: add left_max - height[left] to the answer
- Else do the symmetric logic on the right side.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def trap(height: List[int]) -> int:
    """
    Compute how much water can be trapped after raining.

    Args:
        height: A list of non-negative integers where each value represents the height of a bar.

    Returns:
        The total amount of trapped rain water.
    """
    n = len(height)
    if n < 3:
        return 0

    left: int = 0
    right: int = n - 1
    left_max: int = 0
    right_max: int = 0
    trapped: int = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped += right_max - height[right]
            right -= 1

    return trapped


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

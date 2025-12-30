"""
Problem: Trapping Rain Water

Source: https://leetcode.com/problems/trapping-rain-water/

Difficulty: Hard

Approach: Two pointers tracking left and right max heights

Time Complexity: O(n)

Space Complexity: O(1)
"""

from typing import List


def trap(height: List[int]) -> int:
    """
    Calculate how much water can be trapped after raining.

    Args:
        height: List of non-negative integers representing elevation map
        
    Returns:
        Total amount of water that can be trapped.
        
    Edge Cases:
        - Empty array returns 0
        - Less than 3 bars returns 0
        - All increasing/decreasing heights return 0
        - Flat sections handled correctly
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

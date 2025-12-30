"""
Problem: Container With Most Water

Source: https://leetcode.com/problems/container-with-most-water/

Difficulty: Medium

Approach: Two pointers moving inward from both ends, always moving the shorter line

Time Complexity: O(n)

Space Complexity: O(1)
"""
from typing import List


def max_area(height: List[int]) -> int:
    """
    Find the maximum area of water that can be contained.
    
    Args:
        height: List of non-negative integers representing heights of vertical lines
        
    Returns:
        Maximum area that can be formed between any two lines.
        
    Edge Cases:
        - Empty array returns 0
        - Single element returns 0
        - Two elements returns min(height[0], height[1]) * 1
        - All zero heights return 0
    """
    max_area_result = 0
    left, right = 0, len(height) - 1
    
    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        max_area_result = max(max_area_result, min_height * width)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area_result

"""
Problem: Container With Most Water
Source: https://leetcode.com/problems/container-with-most-water/
Difficulty: Medium

Approach:
- Use two pointers starting from both ends of the array
- Calculate area between the two pointers and update max_area
- Move the pointer pointing to the shorter line inwards
- Continue until the two pointers meet

Time Complexity: O(n) - Single pass with two pointers
Space Complexity: O(1) - Constant space is used
"""
from typing import List

def max_area(height: List[int]) -> int:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water a container can store.
    """
    max_area = 0
    left, right = 0, len(height) - 1
    
    while left < right:
        # Calculate the area between left and right pointers
        h = min(height[left], height[right])
        w = right - left
        max_area = max(max_area, h * w)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area


# Test cases
if __name__ == "__main__":
    # Test case 1: Example from LeetCode
    assert max_area([1,8,6,2,5,4,8,3,7]) == 49
    
    # Test case 2: Only two elements
    assert max_area([1, 1]) == 1
    
    # Test case 3: All elements same height
    assert max_area([5, 5, 5, 5, 5]) == 20
    
    # Test case 4: Increasing heights
    assert max_area([1, 2, 3, 4, 5]) == 6
    
    # Test case 5: Decreasing heights
    assert max_area([5, 4, 3, 2, 1]) == 6
    
    # Test case 6: Random heights
    assert max_area([2, 3, 4, 5, 18, 17, 6]) == 17
    
    print("All test cases passed!")

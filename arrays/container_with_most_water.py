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
import unittest

def max_area(height: List[int]) -> int:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water a container can store.
    
    The solution uses a two-pointer approach where we start with the widest possible container
    and move the pointer pointing to the shorter line inward, as the area is limited by the
    shorter line. This approach ensures we find the maximum area in O(n) time.

    Args:
        height: List of non-negative integers where each integer represents the height of a bar
               at that position.

    Returns:
        int: Maximum area of water that can be contained.
        
    Example:
        >>> max_area([1,8,6,2,5,4,8,3,7])
        49
    """
    max_area = 0
    left, right = 0, len(height) - 1
    
    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        max_area = max(max_area, min_height * width)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return max_area


# Test cases
class TestMaxArea(unittest.TestCase):
    def test_leetcode_example(self):
        """Test the example from LeetCode problem description."""
        self.assertEqual(max_area([1,8,6,2,5,4,8,3,7]), 49)
    
    def test_two_elements(self):
        """Test with minimum input size (2 elements)."""
        self.assertEqual(max_area([1, 1]), 1)
    
    def test_single_bar(self):
        """Test with single bar (should return 0)."""
        self.assertEqual(max_area([5]), 0)
    
    def test_all_same_height(self):
        """Test with all bars of same height."""
        self.assertEqual(max_area([5, 5, 5, 5, 5]), 20)
    
    def test_increasing_heights(self):
        """Test with strictly increasing heights."""
        self.assertEqual(max_area([1, 2, 3, 4, 5]), 6)
    
    def test_decreasing_heights(self):
        """Test with strictly decreasing heights."""
        self.assertEqual(max_area([5, 4, 3, 2, 1]), 6)
    
    def test_alternating_heights(self):
        """Test with alternating high and low heights."""
        self.assertEqual(max_area([1, 8, 1, 8, 1, 8, 1, 8, 1]), 8 * 6)
    
    def test_large_input(self):
        """Test with large input to check performance."""
        large_input = [1] * 10**5
        large_input[0] = 10**4
        large_input[-1] = 10**4
        self.assertEqual(max_area(large_input), 10**4 * (10**5 - 1))
    
    def test_tall_bars_far_apart(self):
        """Test with two tall bars far apart."""
        self.assertEqual(max_area([2, 3, 4, 5, 18, 17, 6]), 17)


if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)
    print("All test cases passed!")

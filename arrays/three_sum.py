"""
Problem: 3Sum
Source: https://leetcode.com/problems/3sum/
Difficulty: Medium

Approach:
- Sort the array to enable two-pointer technique
- Use a for loop to fix one number (nums[i])
- Use two pointers (left, right) to find pairs that sum to -nums[i]
- Skip duplicates to avoid duplicate triplets

Time Complexity: O(n²) - n log n for sorting, then O(n²) for the nested loops
Space Complexity: O(1) - if we don't count the output space
"""
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    
    Args:
        nums: List of integers to search for triplets
        
    Returns:
        List of unique triplets that sum to zero, where each triplet is sorted in
        ascending order.
        
    Example:
        >>> three_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
    """
    nums.sort()
    nums_length = len(nums)
    result = []
    
    for i in range(nums_length - 2):
        # Early termination if the smallest number is greater than 0
        if nums[i] > 0:
            break
            
        # Skip duplicate values for i (after first element)
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left, right = i + 1, nums_length - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicate values for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate values for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
                
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
    return result


# Test cases
if __name__ == "__main__":
    import unittest

    class TestThreeSum(unittest.TestCase):
        def test_three_sum_leetcode_example(self):
            """Test the example from LeetCode problem description."""
            self.assertEqual(
                three_sum([-1, 0, 1, 2, -1, -4]),
                [[-1, -1, 2], [-1, 0, 1]]
            )
        
        def test_all_zeros(self):
            """Test with multiple zeros."""
            self.assertEqual(
                three_sum([0, 0, 0, 0]),
                [[0, 0, 0]]
            )
        
        def test_no_valid_triplets(self):
            """Test when no valid triplets exist."""
            self.assertEqual(three_sum([-2, 0, 1]), [])
        
        def test_duplicate_elements(self):
            """Test with duplicate elements in the input."""
            self.assertEqual(
                three_sum([-1, 0, -1, 0, 1, 1]),
                [[-1, 0, 1]]
            )
        
        def test_all_negative_numbers(self):
            """Test with all negative numbers that can form valid triplets."""
            result = three_sum([-1, -2, -3, 4, 5, 6])
            # Check that all expected triplets are in the result
            self.assertEqual(len(result), 2)
            self.assertIn([-3, -2, 5], result)
            self.assertIn([-3, -1, 4], result)
        
        def test_minimum_length(self):
            """Test with exactly 3 elements (minimum input size)."""
            self.assertEqual(three_sum([-1, 0, 1]), [[-1, 0, 1]])
            self.assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])
        
        def test_short_input(self):
            """Test with input length less than 3."""
            self.assertEqual(three_sum([1, 2]), [])
            self.assertEqual(three_sum([]), [])
        
        def test_all_positive_numbers(self):
            """Test with all positive numbers (no valid triplet)."""
            self.assertEqual(three_sum([1, 2, 3, 4]), [])
    
    unittest.main(argv=[''], exit=False)
    print("All test cases passed!")

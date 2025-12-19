"""
Problem: Two Sum
Source: LeetCode #1
Difficulty: Easy

Approach:
- Use a hash map to store each number's index while iterating through the array.
- For each number, calculate its complement (target - current number).
- If the complement exists in the hash map, return the indices of both numbers.
- This approach ensures we only need to traverse the list once.

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(n) - Store at most n elements in the hash map
"""

from typing import List, Tuple, Optional
import unittest


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices whose values sum to target
        
    Raises:
        ValueError: If no solution is found
        
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("No two sum solution found")


def two_sum_sorted(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    Find two numbers that add up to target in a sorted array.
    
    Args:
        nums: Sorted list of integers in ascending order
        target: Target sum
        
    Returns:
        Tuple of two values that sum to target, or None if not found
        
    Example:
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        (2, 7)
    """
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (nums[left], nums[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None


class TestTwoSum(unittest.TestCase):
    """Test cases for two_sum function"""
    
    def test_basic_case(self):
        """Test basic case with valid solution"""
        self.assertEqual(sorted(two_sum([2, 7, 11, 15], 9)), [0, 1])
        
    def test_duplicate_numbers(self):
        """Test case with duplicate numbers"""
        self.assertEqual(sorted(two_sum([3, 2, 4], 6)), [1, 2])
        
    def test_same_number_twice(self):
        """Test case where same number is used twice"""
        self.assertEqual(sorted(two_sum([3, 3], 6)), [0, 1])
        
    def test_negative_numbers(self):
        """Test case with negative numbers"""
        self.assertEqual(sorted(two_sum([-1, -2, -3, -4, -5], -8)), [2, 4])
        
    def test_no_solution(self):
        """Test case with no valid solution"""
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 10)


class TestTwoSumSorted(unittest.TestCase):
    """Test cases for two_sum_sorted function"""
    
    def test_basic_case(self):
        """Test basic case with valid solution"""
        self.assertEqual(two_sum_sorted([2, 7, 11, 15], 9), (2, 7))
        
    def test_adjacent_elements(self):
        """Test case with adjacent elements as solution"""
        self.assertEqual(two_sum_sorted([1, 2, 3, 4, 5], 7), (2, 5))
        
    def test_negative_numbers(self):
        """Test case with negative numbers"""
        self.assertEqual(two_sum_sorted([-5, -3, -2, 0, 1], -2), (-3, 1))
        
    def test_no_solution(self):
        """Test case with no valid solution"""
        self.assertIsNone(two_sum_sorted([1, 2, 3], 10))


if __name__ == "__main__":
    unittest.main()

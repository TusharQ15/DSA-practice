"""
Problem: Two Sum
Source: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Approach:
1. Hash Map: Use a dictionary to store seen values and their indices.
   For each number, check if its complement (target - num) exists in the dictionary.
   This approach runs in O(n) time with O(n) space.

2. Two Pointers (For Sorted Arrays): If the array is sorted, use two pointers
   to find the pair that sums to the target. This runs in O(n) time with O(1) space.

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(n) - Store up to n elements in the hash map
"""

def two_sum(nums, target):
    """
    Find indices of two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices whose values sum to target
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def two_sum_sorted(nums, target):
    """
    Find two numbers that add up to target in a sorted array.
    Returns the actual values, not indices.
    
    Args:
        nums: Sorted list of integers
        target: Target sum
        
    Returns:
        List of two values that sum to target
    """
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [nums[left], nums[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

if __name__ == "__main__":
    import unittest
    
    class TestTwoSum(unittest.TestCase):
        def test_two_sum(self):
            test_cases = [
                ([2, 7, 11, 15], 9, [0, 1]),
                ([3, 2, 4], 6, [1, 2]),
                ([3, 3], 6, [0, 1]),
                ([1, 2, 3, 4, 5], 9, [3, 4]),
                ([-1, -2, -3, -4, -5], -8, [2, 4])
            ]
            
            for nums, target, expected in test_cases:
                with self.subTest(nums=nums, target=target):
                    result = two_sum(nums, target)
                    self.assertEqual(result, expected)
        
        def test_two_sum_sorted(self):
            test_cases = [
                ([2, 7, 11, 15], 9, [2, 7]),
                ([2, 3, 4], 6, [2, 4]),
                ([-1, 0], -1, [-1, 0])
            ]
            
            for nums, target, expected in test_cases:
                with self.subTest(nums=nums, target=target):
                    result = two_sum_sorted(nums, target)
                    self.assertEqual(result, expected)
    
    unittest.main(argv=[''], exit=False)

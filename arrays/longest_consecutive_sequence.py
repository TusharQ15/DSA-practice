"""
Problem: Longest Consecutive Sequence
Source: https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium

Approach:
The solution uses a hash set to store all numbers for O(1) lookups. We iterate through each number,
and for each number that is the start of a sequence (i.e., num-1 is not in the set),
we count how many consecutive numbers follow it. The maximum count is our answer.

Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            max_length = max(max_length, current_streak)
    
    return max_length


import unittest


class TestLongestConsecutiveSequence(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
    
    def test_with_duplicates(self):
        self.assertEqual(longest_consecutive([1, 2, 2, 3, 4, 4, 5]), 5)
    
    def test_empty_list(self):
        self.assertEqual(longest_consecutive([]), 0)
    
    def test_single_element(self):
        self.assertEqual(longest_consecutive([5]), 1)
    
    def test_already_sorted(self):
        self.assertEqual(longest_consecutive([1, 2, 3, 4, 5]), 5)
    
    def test_negative_numbers(self):
        self.assertEqual(longest_consecutive([-1, -2, 0, 1, 3, 4, 5]), 4)  # Sequence: [-2, -1, 0, 1]


if __name__ == "__main__":
    unittest.main()

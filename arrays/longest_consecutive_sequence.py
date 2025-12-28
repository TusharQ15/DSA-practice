"""
Problem: Longest Consecutive Sequence

Source: https://leetcode.com/problems/longest-consecutive-sequence/

Difficulty: Medium

Approach:
- Convert input to a set for O(1) lookups
- Only start counting from the smallest number in a sequence (num-1 not in set)
- Expand right to find the full sequence length
- Track the maximum sequence length found

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Set

def longest_consecutive(nums: List[int]) -> int:
    """
    Find the length of the longest consecutive elements sequence.
    
    Args:
        nums: List of integers (can be unsorted and contain duplicates)
    
    Returns:
        Length of the longest consecutive sequence
    """
    num_set = set(nums)
    longest = 0
    
    for num in num_set:
        # Only start counting from the smallest number in a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Expand to the right as far as possible
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                
            # Update the longest sequence found
            longest = max(longest, current_length)
    
    return longest


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

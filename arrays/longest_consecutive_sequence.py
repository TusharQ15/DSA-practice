"""
Problem: Longest Consecutive Sequence

Source: https://leetcode.com/problems/longest-consecutive-sequence/

Difficulty: Medium

Approach:
Use a hash set to achieve O(1) average lookups. For each number, treat it as the start of a sequence
only if (num - 1) is not in the set. Then, count how long the sequence continues by checking
(num + 1), (num + 2), etc. Track the maximum length encountered.

Time Complexity: O(n) on average, where n is the number of elements.
Space Complexity: O(n) for the hash set.
"""

from typing import List, Set


def longest_consecutive(nums: List[int]) -> int:
    """
    Find the length of the longest sequence of consecutive integers in an unsorted array.

    Args:
        nums: A list of integers (can contain duplicates and be unsorted).

    Returns:
        The length of the longest consecutive elements sequence.
    """
    if not nums:
        return 0

    num_set: Set[int] = set(nums)
    longest: int = 0

    for num in num_set:
        # Only start counting from numbers that are the beginning of a sequence
        if num - 1 not in num_set:
            current_length: int = 1
            current_value: int = num

            while current_value + 1 in num_set:
                current_value += 1
                current_length += 1

            if current_length > longest:
                longest = current_length

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

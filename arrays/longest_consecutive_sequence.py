"""
Problem: Longest Consecutive Sequence

Source: https://leetcode.com/problems/longest-consecutive-sequence/

Difficulty: Medium

Approach: Hash set to find sequence starts and expand forward

Time Complexity: O(n)

Space Complexity: O(n)
"""

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Find the length of the longest consecutive elements sequence.

    Args:
        nums: List of integers (can be unsorted and contain duplicates)
        
    Returns:
        Length of the longest consecutive sequence.
        
    Edge Cases:
        - Empty array returns 0
        - Single element returns 1
        - All duplicates returns 1
        - Negative numbers handled correctly
        - Mixed positive/negative handled correctly
    """
    if not nums:
        return 0

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
            if current_length > longest:
                longest = current_length

    return longest

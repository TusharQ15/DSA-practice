"""
Problem: Group Anagrams

Source: https://leetcode.com/problems/group-anagrams/

Difficulty: Medium

Approach:
- Use a hash map from sorted string or character count signature to list of words.
- Sorting each string or building a frequency tuple creates a stable key for grouping.
- Collect all strings with the same signature into groups.

Time Complexity: O(n * k log k) where n is number of strings, k is average string length
Space Complexity: O(n * k) for storing groups and hash map
"""

from typing import List, Dict
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together from a list of strings.
    
    Args:
        strs: List of strings to group
        
    Returns:
        List of groups where each group contains anagrams
        
    Example:
        Input: ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    """
    groups: Dict[str, List[str]] = defaultdict(list)
    
    for string in strs:
        # Create signature by sorting characters
        signature = ''.join(sorted(string))
        groups[signature].append(string)
    
    return list(groups.values())

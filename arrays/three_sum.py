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
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    """
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n - 2):
        # Early termination if the smallest number is greater than 0
        if nums[i] > 0:
            break
            
        # Skip duplicate values for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left, right = i + 1, n - 1
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

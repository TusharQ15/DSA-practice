"""
Problem: 3Sum

Source: https://leetcode.com/problems/3sum/

Difficulty: Medium

Approach: Sort array and use two-pointer technique for each fixed element

Time Complexity: O(n²)

Space Complexity: O(1) excluding output space
"""
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.
    
    Args:
        nums: List of integers (may contain duplicates, positive and negative)
        
    Returns:
        List of unique triplets [a, b, c] where a + b + c == 0.
        Each triplet is sorted in ascending order, and the result list contains no duplicates.
        
    Edge Cases:
        - Empty array returns empty list
        - Array with less than 3 elements returns empty list
        - All zeros returns [[0, 0, 0]]
        - No valid triplets returns empty list
    """
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n - 2):
        # Early termination if the smallest number is greater than 0
        if nums[i] > 0:
            break
            
        # Skip duplicate values for i (after first element)
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

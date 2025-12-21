"""
Problem: Maximum Product Subarray
Source: https://leetcode.com/problems/maximum-product-subarray/
Difficulty: Medium

Approach:
- Track both maximum and minimum products at each step since a negative number can make a minimum product the maximum when multiplied by another negative.
- Update the current maximum and minimum by considering the current number, current max * number, and current min * number.
- Keep track of the global maximum product seen so far.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) as we use constant extra space
"""

from typing import List

def max_product(nums: List[int]) -> int:
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for num in nums[1:]:
        if num < 0:
            max_prod, min_prod = min_prod, max_prod  # Swap max and min when current number is negative
        
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        
        result = max(result, max_prod)
    
    return result

# Test cases
import unittest

class TestMaxProduct(unittest.TestCase):
    def test_max_product(self):
        self.assertEqual(max_product([2,3,-2,4]), 6)
        self.assertEqual(max_product([-2,0,-1]), 0)
        self.assertEqual(max_product([-2,3,-4]), 24)
        self.assertEqual(max_product([0,2]), 2)
        self.assertEqual(max_product([-2]), -2)
        self.assertEqual(max_product([3,-1,4]), 4)

if __name__ == '__main__':
    unittest.main()

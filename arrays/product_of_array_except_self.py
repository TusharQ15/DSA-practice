"""
Problem: Product of Array Except Self
Source: https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium

Approach:
1. Calculate prefix products from left to right
2. Calculate suffix products from right to left
3. Multiply corresponding prefix and suffix products to get the result

Time Complexity: O(n) - Three passes through the array
Space Complexity: O(1) - Output array is not considered extra space
"""
from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    
    # Calculate prefix products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Calculate suffix products and multiply with prefix
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result


import unittest

class TestProductExceptSelf(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 2, 3, 4]
        expected = [24, 12, 8, 6]
        self.assertEqual(product_except_self(nums), expected)
    
    def test_example_2(self):
        nums = [-1, 1, 0, -3, 3]
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(product_except_self(nums), expected)
    
    def test_two_elements(self):
        nums = [2, 3]
        expected = [3, 2]
        self.assertEqual(product_except_self(nums), expected)
    
    def test_with_negative_numbers(self):
        nums = [-1, -2, -3, -4]
        expected = [-24, -12, -8, -6]
        self.assertEqual(product_except_self(nums), expected)
    
    def test_with_zero(self):
        nums = [1, 0, 4, 2]
        expected = [0, 8, 0, 0]
        self.assertEqual(product_except_self(nums), expected)


if __name__ == "__main__":
    unittest.main()

"""
Problem: Best Time to Buy and Sell Stock
Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy

Approach:
- Track the minimum price seen so far.
- Calculate potential profit if sold at current price.
- Update maximum profit if current potential profit is greater.
- Return the maximum profit found.

Time Complexity: O(n) where n is the number of prices
Space Complexity: O(1) as we use constant extra space
"""

from typing import List

def max_profit(prices: List[int]) -> int:
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

# Test cases
import unittest

class TestMaxProfit(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(max_profit([7,1,5,3,6,4]), 5)
        self.assertEqual(max_profit([7,6,4,3,1]), 0)
        self.assertEqual(max_profit([1,2]), 1)
        self.assertEqual(max_profit([2,4,1]), 2)
        self.assertEqual(max_profit([3,2,6,5,0,3]), 4)
        self.assertEqual(max_profit([1]), 0)

if __name__ == '__main__':
    unittest.main()

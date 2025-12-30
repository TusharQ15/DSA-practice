"""
Problem: Best Time to Buy and Sell Stock

Source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Difficulty: Easy

Approach: Track minimum price seen so far and calculate maximum profit

Time Complexity: O(n)

Space Complexity: O(1)
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Find the maximum profit that can be achieved by buying and selling a stock once.
    
    Args:
        prices: List of non-negative integers where prices[i] is the price of the stock on day i
        
    Returns:
        Maximum profit possible from one transaction (buy then sell).
        Returns 0 if no profit is possible.
        
    Edge Cases:
        - Empty array returns 0
        - Single element returns 0
        - All decreasing prices returns 0
        - All same prices returns 0
    """
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit_result = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit_result = max(max_profit_result, price - min_price)
    
    return max_profit_result

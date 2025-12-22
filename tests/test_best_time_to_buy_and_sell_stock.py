"""
Tests for Best Time to Buy and Sell Stock problem
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from arrays.best_time_to_buy_and_sell_stock import max_profit

def test_max_profit_basic():
    # Basic test cases
    assert max_profit([7,1,5,3,6,4]) == 5  # Buy at 1, sell at 6
    assert max_profit([7,6,4,3,1]) == 0    # No transactions possible
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4  # Multiple peaks and valleys

def test_max_profit_edge_cases():
    # Edge cases
    assert max_profit([]) == 0              # Empty input
    assert max_profit([1]) == 0             # Single day
    assert max_profit([1, 5]) == 4          # Two days, increasing
    assert max_profit([5, 1]) == 0          # Two days, decreasing
    assert max_profit([2, 4, 1]) == 2       # Multiple days, peak in middle
    assert max_profit([3, 3, 3, 3, 3]) == 0 # All same prices
    assert max_profit([2, 1, 2, 1, 0, 1, 2]) == 2  # Multiple valleys and peaks
    assert max_profit([2, 4, 1, 7, 5, 3, 6, 4]) == 6  # Multiple possible profits
    assert max_profit([5, 5, 5, 5, 5]) == 0  # All same prices (different input)

def test_max_profit_large_input():
    # Large input with increasing prices
    large_increasing = list(range(100000))
    assert max_profit(large_increasing) == 99999
    
    # Large input with decreasing prices
    large_decreasing = list(range(100000, 0, -1))
    assert max_profit(large_decreasing) == 0

"""
Tests for array problems
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from arrays.two_sum import two_sum

def test_two_sum():
    """Test cases for two_sum function"""
    # Test case 1: Basic test case
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case 2: Numbers not at beginning
    assert two_sum([3, 2, 4], 6) == [1, 2]
    
    # Test case 3: Duplicate numbers
    assert two_sum([3, 3], 6) == [0, 1]
    
    # Test case 4: No solution (function should return empty list)
    assert two_sum([1, 2, 3], 7) == []
    
    # Test case 5: Negative numbers
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

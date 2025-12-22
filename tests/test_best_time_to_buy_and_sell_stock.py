"""
Tests for Best Time to Buy and Sell Stock problem
"""
import sys
import os
import unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from arrays.best_time_to_buy_and_sell_stock import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_max_profit(self):
        """Test cases for max_profit function"""
        # Test case 1: Regular case with profit
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
        
        # Test case 2: Prices always decreasing, no profit possible
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)
        
        # Test case 3: Only two days, with profit
        self.assertEqual(max_profit([1, 2]), 1)
        
        # Test case 4: Price drops then rises
        self.assertEqual(max_profit([2, 4, 1]), 2)
        
        # Test case 5: Multiple peaks and valleys
        self.assertEqual(max_profit([3, 2, 6, 5, 0, 3]), 4)
        
        # Test case 6: Single day
        self.assertEqual(max_profit([1]), 0)
        
        # Test case 7: Empty list
        self.assertEqual(max_profit([]), 0)
        
        # Test case 8: Multiple same prices
        self.assertEqual(max_profit([5, 5, 5, 5, 5]), 0)

def test_max_profit():
    """Function to run all max profit tests"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxProfit)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    test_max_profit()

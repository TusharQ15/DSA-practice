import unittest
from typing import List
from arrays.three_sum import three_sum

class TestThreeSum(unittest.TestCase):
    def test_three_sum(self):
        # Test case from the problem
        self.assertCountEqual(
            three_sum([-1, 0, 1, 2, -1, -4]),
            [[-1, -1, 2], [-1, 0, 1]]
        )
        
        # Test with no valid triplets
        self.assertEqual(three_sum([0, 1, 1]), [])
        
        # Test with all zeros
        self.assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])
        
        # Test with multiple valid triplets
        self.assertCountEqual(
            three_sum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]),
            [[-4, 0, 4], [-4, 1, 3], [-3, -1, 4], [-3, 0, 3], 
             [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, -1, 2], 
             [-1, 0, 1]]
        )
        
        # Test with empty input
        self.assertEqual(three_sum([]), [])
        
        # Test with less than 3 elements
        self.assertEqual(three_sum([1, 2]), [])

if __name__ == '__main__':
    unittest.main()

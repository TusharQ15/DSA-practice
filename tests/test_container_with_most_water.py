import unittest
from arrays.container_with_most_water import max_area

class TestContainerWithMostWater(unittest.TestCase):
    def test_max_area(self):
        # Test case from the problem
        self.assertEqual(max_area([1,8,6,2,5,4,8,3,7]), 49)
        
        # Test with only two elements
        self.assertEqual(max_area([1, 1]), 1)
        
        # Test with all elements same height
        self.assertEqual(max_area([5, 5, 5, 5, 5]), 20)
        
        # Test with increasing heights
        self.assertEqual(max_area([1, 2, 3, 4, 5]), 6)
        
        # Test with decreasing heights
        self.assertEqual(max_area([5, 4, 3, 2, 1]), 6)
        
        # Test with random heights
        self.assertEqual(max_area([2, 3, 4, 5, 18, 17, 6]), 17)
        
        # Test with only one element (should return 0 as no container can be formed)
        self.assertEqual(max_area([5]), 0)

if __name__ == '__main__':
    unittest.main()

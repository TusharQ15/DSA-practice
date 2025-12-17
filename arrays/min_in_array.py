"""
Problem: Find Minimum Element in Array
Source: Common DSA Problem
Difficulty: Easy

Approach:
1. Initialize the first element as the minimum.
2. Iterate through the array, updating the minimum when a smaller element is found.
3. Return the final minimum value.

Time Complexity: O(n) - We need to check each element once
Space Complexity: O(1) - Only constant extra space is used
"""

def find_min(arr):
    """
    Find the minimum element in a list of integers.
    
    Args:
        arr: List of integers to find the minimum from
        
    Returns:
        The minimum element in the list
        
    Raises:
        ValueError: If the input list is empty
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not arr:
        raise ValueError("Input list cannot be empty")
        
    min_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
    return min_val

def find_min_builtin(arr):
    """
    Find minimum using Python's built-in min() function.
    This is for comparison and demonstration purposes.
    
    Args:
        arr: List of numbers to find the minimum from
        
    Returns:
        The minimum element in the list
        
    Raises:
        ValueError: If the input list is empty
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not arr:
        raise ValueError("Input list cannot be empty")
    return min(arr)

if __name__ == "__main__":
    import unittest
    
    class TestMinInArray(unittest.TestCase):
        def test_find_min(self):
            test_cases = [
                ([5, 2, 8, 1, 9], 1),     # Unsorted
                ([1, 2, 3, 4, 5], 1),     # Sorted ascending
                ([5, 4, 3, 2, 1], 1),     # Sorted descending
                ([1], 1),                  # Single element
                ([-1, -2, -3, -4, -5], -5),  # Negative numbers
                ([10, 5, 10, 5, 10], 5),   # Duplicate minimum
                ([2, 4, 6, 8, 10, 9, 7, 5, 3, 1], 1)  # Minimum at the end
            ]
            
            for arr, expected in test_cases:
                with self.subTest(arr=arr):
                    self.assertEqual(find_min(arr), expected)
        
        def test_find_min_builtin(self):
            test_cases = [
                ([5, 2, 8, 1, 9], 1),
                ([1, 2, 3, 4, 5], 1),
                ([1], 1)
            ]
            
            for arr, expected in test_cases:
                with self.subTest(arr=arr):
                    self.assertEqual(find_min_builtin(arr), expected)
        
        def test_invalid_input(self):
            with self.assertRaises(TypeError):
                find_min("not a list")
            with self.assertRaises(ValueError):
                find_min([])
            with self.assertRaises(TypeError):
                find_min_builtin(123)
            with self.assertRaises(ValueError):
                find_min_builtin([])
    
    unittest.main(argv=[''], exit=False)

# Warm-up problem (not an interview-level question)
"""
Problem: Sum of Array Elements
Source: Common DSA Problem

Given an array of numbers, calculate the sum of all elements.

Approaches:
1. Iterative Sum:
   - Initialize total to 0
   - Add each element to total
   - O(n) time, O(1) space

2. Built-in Sum:
   - Use Python's built-in sum()
   - Clean and efficient
   - O(n) time, O(1) space

Time Complexity: O(n) - Must visit each element once
Space Complexity: O(1) - Constant extra space used
"""

def sum_array_iterative(arr):
    """
    Calculate sum of array elements using iteration.
    
    Args:
        arr (list): List of numbers (int/float)
        
    Returns:
        int/float: Sum of array elements
        
    Raises:
        TypeError: If input is not a list
        ValueError: If list is empty
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not arr:
        raise ValueError("Cannot calculate sum of empty list")
        
    total = 0
    for num in arr:
        total += num
    return total

def sum_array_builtin(arr):
    """
    Calculate sum using Python's built-in sum().
    
    Args:
        arr (list): List of numbers (int/float)
        
    Returns:
        int/float: Sum of array elements
        
    Raises:
        TypeError: If input is not a list
        ValueError: If list is empty
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not arr:
        raise ValueError("Cannot calculate sum of empty list")
    return sum(arr)

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 15),          # Positive integers
        ([-1, -2, -3, -4, -5], -15),    # Negative integers
        ([1, -2, 3, -4, 5], 3),         # Mixed signs
        ([0, 0, 0, 0, 0], 0),           # All zeros
        ([7], 7),                        # Single element
        ([1.5, 2.5, 3.5], 7.5),         # Floats
        ([-1, 0, 1], 0),                # Sum to zero
        ([10**6] * 1000, 10**9),        # Large numbers
    ]
    
    print("=== Testing Array Sum ===\n")
    
    # Test iterative implementation
    print("Testing iterative implementation:")
    print("=" * 50)
    for arr, expected in test_cases:
        result = sum_array_iterative(arr)
        print(f"Array: {arr}")
        print(f"Sum:   {result}")
        assert result == expected, f"Expected {expected}, got {result}"
        print(" Test passed")
        print("-" * 50)
    
    # Test built-in implementation
    print("\nTesting built-in sum() implementation:")
    print("=" * 50)
    for arr, expected in test_cases:
        result = sum_array_builtin(arr)
        print(f"Array: {arr}")
        print(f"Sum:   {result}")
        assert result == expected, f"Expected {expected}, got {result}"
        print(" Test passed")
        print("-" * 50)
    
    # Test error handling
    print("\nTesting error handling:")
    print("=" * 50)
    
    # Test empty list
    try:
        sum_array_iterative([])
    except ValueError as e:
        print(f"Test passed: {e}")
    
    # Test invalid input type
    try:
        sum_array_builtin("not a list")
    except TypeError as e:
        print(f"Test passed: {e}")
    
    # Test None input
    try:
        sum_array_iterative(None)
    except TypeError as e:
        print(f"Test passed: {e}")

# Warm-up problem (not an interview-level question)
"""
Problem: Calculate Average of Array Elements
Source: Common DSA Problem
Difficulty: Easy

Approach: Calculate the arithmetic mean of all elements in the array.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List, Union

def calculate_average(arr: List[Union[int, float]]) -> float:
    """
    Calculate average of array elements.
    
    Args:
        arr: List of numbers (int/float)
        
    Returns:
        Arithmetic mean of array elements
        
    Raises:
        ValueError: If list is empty
    """
    if not arr:
        raise ValueError("Cannot calculate average of empty list")
    return sum(arr) / len(arr)

def calculate_average_manual(arr: List[Union[int, float]]) -> float:
    """
    Calculate average by manual iteration.
    
    Args:
        arr: List of numbers (int/float)
        
    Returns:
        Arithmetic mean of array elements
        
    Raises:
        ValueError: If list is empty
    """
    if not arr:
        raise ValueError("Cannot calculate average of empty list")
        
    total = 0.0
    count = 0
    for num in arr:
        total += num
        count += 1
    return total / count

if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [1, 2, 3, 4, 5],          # Positive integers
        [-2, -1, 0, 1, 2],        # Mixed signs, zero sum
        [1.5, 2.5, 3.5],          # Floating point numbers
        [10],                     # Single element
        [0, 0, 0, 0],             # All zeros
        [-1, -2, -3, -4, -5]      # Negative numbers
    ]
    
    for arr in test_arrays:
        avg1 = calculate_average(arr)
        avg2 = calculate_average_manual(arr)
        expected = sum(arr) / len(arr)
        assert abs(avg1 - expected) < 1e-9, f"Failed for {arr}"
        assert abs(avg2 - expected) < 1e-9, f"Failed for {arr}"
    
    # Test empty list
    try:
        calculate_average([])
        assert False, "Expected ValueError for empty list"
    except ValueError:
        pass
    
    # Test error handling
    print("=== Testing Array Average ===\n")
    
    # Test sum/len implementation
    print("Testing sum()/len() implementation:")
    print("=" * 50)
    for arr in test_arrays:
        result = calculate_average(arr)
        print(f"Array: {arr}")
        print(f"Average: {result:.2f}")
        print(" Test passed")
        print("-" * 50)
    
    # Test manual implementation
    print("\nTesting manual implementation:")
    print("=" * 50)
    for arr in test_arrays:
        result = calculate_average_manual(arr)
        print(f"Array: {arr}")
        print(f"Average: {result:.2f}")
        print(" Test passed")
        print("-" * 50)
    
    # Test error handling
    print("\nTesting error handling:")
    print("=" * 50)
    
    # Test empty list
    try:
        calculate_average([])
    except ValueError as e:
        print(f"Test passed: {e}")
    
    # Test invalid input type
    try:
        calculate_average_manual("not a list")
    except TypeError as e:
        print(f"Test passed: {e}")
    
    # Test None input
    try:
        calculate_average_manual(None)
    except TypeError as e:
        print(f"Test passed: {e}")

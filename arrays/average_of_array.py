"""
Problem: Calculate Average of Array Elements
Source: Common DSA Problem

Given an array of numbers, calculate the arithmetic mean.

Approaches:
1. Using sum() and len():
   - Sum all elements and divide by count
   - Simple and readable
   - O(n) time, O(1) space

2. Manual Calculation:
   - Iterate through elements
   - Accumulate sum and count
   - O(n) time, O(1) space

Time Complexity: O(n) - Must visit each element once
Space Complexity: O(1) - Constant extra space used
"""

def calculate_average(arr):
    """
    Calculate average using Python's sum() and len().
    
    Args:
        arr (list): List of numbers (int/float)
        
    Returns:
        float: Arithmetic mean of array elements
        
    Raises:
        TypeError: If input is not a list
        ValueError: If list is empty
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not arr:
        raise ValueError("Cannot calculate average of empty list")
        
    return sum(arr) / len(arr)

def calculate_average_manual(arr):
    """
    Calculate average by manual iteration.
    
    Args:
        arr (list): List of numbers (int/float)
        
    Returns:
        float: Arithmetic mean of array elements
        
    Raises:
        TypeError: If input is not a list
        ValueError: If list is empty
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if not arr:
        raise ValueError("Cannot calculate average of empty list")
        
    total = 0.0  # Use float to handle integer division
    count = 0
    for num in arr:
        total += num
        count += 1
    return total / count

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3.0),          # Positive integers
        ([-2, -1, 0, 1, 2], 0.0),        # Mixed signs, zero sum
        ([10], 10.0),                     # Single element
        ([1.5, 2.5, 3.5], 2.5),           # Floats
        ([0.1, 0.2, 0.3, 0.4], 0.25),     # Small decimals
        ([10**6] * 1000, 10**6),          # Large numbers
        ([-1, 1], 0.0),                   # Cancel out to zero
    ]
    
    print("=== Testing Array Average ===\n")
    
    # Test sum/len implementation
    print("Testing sum()/len() implementation:")
    print("=" * 50)
    for arr, expected in test_cases:
        result = calculate_average(arr)
        print(f"Array: {arr}")
        print(f"Average: {result:.2f}")
        assert abs(result - expected) < 1e-9, f"Expected ~{expected}, got {result}"
        print(" Test passed")
        print("-" * 50)
    
    # Test manual implementation
    print("\nTesting manual implementation:")
    print("=" * 50)
    for arr, expected in test_cases:
        result = calculate_average_manual(arr)
        print(f"Array: {arr}")
        print(f"Average: {result:.2f}")
        assert abs(result - expected) < 1e-9, f"Expected ~{expected}, got {result}"
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

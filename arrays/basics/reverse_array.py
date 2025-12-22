# Warm-up problem (not an interview-level question)
"""
Problem: Reverse Array
Source: Common DSA Problem

Given an array, reverse its elements in-place and/or return a new reversed array.

Approaches:
1. In-place reversal using two pointers:
   - Use start and end pointers
   - Swap elements at these pointers
   - Move pointers towards the center
   - O(n) time, O(1) space

2. Using Python slicing:
   - Return a new reversed array using arr[::-1]
   - O(n) time, O(n) space (creates a new list)

Time Complexity: O(n) - n/2 swaps for in-place, n for slice
Space Complexity: O(1) for in-place, O(n) for slice version
"""

def reverse_array(arr):
    """
    Reverse the elements of an array in-place.
    
    Args:
        arr (list): List to be reversed (modified in-place)
        
    Returns:
        list: The reversed array (same reference as input)
        
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
        
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

def reverse_array_slice(arr):
    """
    Return a new reversed array using Python slicing.
    Original array remains unchanged.
    
    Args:
        arr (list): List to be reversed
        
    Returns:
        list: New list with elements in reverse order
        
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    return arr[::-1]

def reverse_array_recursive(arr, start=0, end=None):
    """
    Reverse array recursively using two pointers.
    
    Args:
        arr (list): List to be reversed (modified in-place)
        start (int): Starting index (default: 0)
        end (int): Ending index (default: len(arr)-1)
        
    Returns:
        list: The reversed array (same reference as input)
    """
    if end is None:
        end = len(arr) - 1
        
    if start >= end:
        return arr
        
    # Swap elements
    arr[start], arr[end] = arr[end], arr[start]
    
    # Recur for the remaining subarray
    return reverse_array_recursive(arr, start + 1, end - 1)

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([1], [1]),
        ([], []),
        (['a', 'b', 'c'], ['c', 'b', 'a']),
        ([1, 2, 3, 2, 1], [1, 2, 3, 2, 1]),  # Palindrome
        ([1.5, 2.5, 3.5], [3.5, 2.5, 1.5]),  # Floats
        ([True, False], [False, True]),       # Booleans
    ]
    
    print("=== Testing Reverse Array ===\n")
    
    # Test in-place reversal
    print("Testing in-place reversal:")
    print("=" * 50)
    for test, expected in test_cases:
        arr = test.copy()
        reverse_array(arr)
        print(f"Original: {test}")
        print(f"Reversed: {arr}")
        assert arr == expected, f"Expected {expected}, got {arr}"
        print(" Test passed")
        print("-" * 50)
    
    # Test slice version
    print("\nTesting slice version (returns new list):")
    print("=" * 50)
    for test, expected in test_cases:
        result = reverse_array_slice(test)
        print(f"Original: {test}")
        print(f"Reversed: {result}")
        print(f"Original unchanged: {test}")
        assert result == expected, f"Expected {expected}, got {result}"
        print(" Test passed")
        print("-" * 50)
    
    # Test recursive version
    print("\nTesting recursive version (in-place):")
    print("=" * 50)
    for test, expected in test_cases:
        arr = test.copy()
        reverse_array_recursive(arr)
        print(f"Original: {test}")
        print(f"Reversed: {arr}")
        assert arr == expected, f"Expected {expected}, got {arr}"
        print(" Test passed")
        print("-" * 50)
    
    # Test error handling
    try:
        reverse_array("not a list")
    except TypeError as e:
        print(f"\nError test passed: {e}")
    
    try:
        reverse_array_slice(123)
    except TypeError as e:
        print(f"Error test passed: {e}")

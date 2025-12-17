"""
Problem: Move Zeroes
Source: https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Approach:
1. Two-pointer technique:
   - Use one pointer (pos) to track the position of the next non-zero element
   - Iterate through the array with another pointer
   - For each non-zero element, place it at pos and increment pos
   - After processing all elements, fill the remaining positions with zeros

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(1) for in-place, O(n) for the non-inplace version
"""

def move_zeros(arr):
    """
    Move all zeros to the end while maintaining the relative order of non-zero elements.
    Returns a new list (non-inplace).
    
    Args:
        arr (list): List of integers
        
    Returns:
        list: New list with all zeros moved to the end
        
    Raises:
        ValueError: If the input is not a list
    """
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    if not arr:
        return []
        
    # Count non-zero elements and create a new list
    non_zeros = [x for x in arr if x != 0]
    zero_count = len(arr) - len(non_zeros)
    
    # Return the new list with zeros at the end
    return non_zeros + [0] * zero_count

def move_zeros_in_place(arr):
    """
    Move all zeros to the end in-place while maintaining the relative order of non-zero elements.
    Modifies the input list.
    
    Args:
        arr (list): List of integers (will be modified in-place)
        
    Returns:
        None: The input list is modified in-place
        
    Raises:
        ValueError: If the input is not a list
    """
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    if not arr:
        return
        
    # Initialize pointer for the position of the next non-zero element
    pos = 0
    
    # Move all non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    
    # Fill the remaining positions with zeros
    while pos < len(arr):
        arr[pos] = 0
        pos += 1

if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),     # Mixed zeros and non-zeros
        ([1, 2, 3, 0, 0, 4], [1, 2, 3, 4, 0, 0]),  # Zeros in the middle and end
        ([0, 0, 1], [1, 0, 0]),                    # Zeros at the beginning
        ([1, 0, 0, 2, 3], [1, 2, 3, 0, 0]),        # Multiple zeros together
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),        # No zeros
        ([0, 0, 0], [0, 0, 0]),                    # All zeros
        ([1], [1]),                                # Single element (non-zero)
        ([0], [0]),                                # Single element (zero)
        ([], [])                                   # Empty list
    ]
    
    print("=== Testing move_zeros (creates new list) ===")
    for test, expected in test_cases:
        print(f"Original: {test}")
        result = move_zeros(test)
        print(f"Result:   {result}")
        assert result == expected, f"Expected {expected}, got {result}"
        print(" Test passed")
        print("-" * 50)
    
    print("\n=== Testing move_zeros_in_place (modifies in-place) ===")
    for test, expected in test_cases:
        # Create a copy since the function modifies in-place
        test_copy = test.copy()
        print(f"Original: {test_copy}")
        move_zeros_in_place(test_copy)
        print(f"Modified: {test_copy}")
        assert test_copy == expected, f"Expected {expected}, got {test_copy}"
        print(" Test passed")
        print("-" * 50)
    
    # Test invalid input
    try:
        move_zeros("not a list")
    except ValueError as e:
        print(f"Test passed: {e}")
    
    try:
        move_zeros_in_place(123)
    except ValueError as e:
        print(f"Test passed: {e}")

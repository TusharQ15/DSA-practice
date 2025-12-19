"""
Problem: Find Maximum Element in Array
Source: Common DSA Problem
Difficulty: Easy

Approach: Iterate through the array while keeping track of the maximum element seen so far.
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List, Optional

def find_max(arr: List[int]) -> int:
    """
    Find the maximum element in a list of integers.
    
    Args:
        arr: List of integers to find the maximum from
        
    Returns:
        The maximum element in the list
        
    Raises:
        ValueError: If the input list is empty
    """
    if not arr:
        raise ValueError("Input list cannot be empty")
        
    max_num = arr[0]
    for num in arr[1:]:
        if num > max_num:
            max_num = num
    return max_num

def find_max_builtin(arr: List[int]) -> int:
    """
    Find maximum using Python's built-in max() function.
    
    Args:
        arr: List of integers to find the maximum from
        
    Returns:
        The maximum element in the list
        
    Raises:
        ValueError: If the input list is empty
    """
    if not arr:
        raise ValueError("Input list cannot be empty")
    return max(arr)

def linear_search(arr: List[int], target: int) -> int:
    """
    Linear search to find a target in an array.
    
    Args:
        arr: List of integers to search in
        target: The element to find
        
    Returns:
        Index of the target if found, -1 otherwise
    """
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

if __name__ == "__main__":
    # Test cases for find_max
    test_arrays = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [-1, -2, -3, -4, -5],
        [10, 9, 11, 8, 12],
        [5, 5, 5, 5, 5]
    ]
    
    print("=== Testing Array Maximum ===\n")
    
    # Test both implementations
    for arr in test_arrays:
        max1 = find_max(arr)
        max2 = find_max_builtin(arr)
        expected = max(arr)
        assert max1 == expected, f"Failed for {arr}"
        assert max2 == expected, f"Failed for {arr}"
        print(f"Array: {arr}")
        print(f"Maximum: {max1}")
        print(" Test passed")
        print("-" * 50)
    
    # Test linear search
    search_tests = [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 6, -1),
        ([], 1, -1),
        ([5], 5, 0)
    ]
    
    print("\n=== Testing Linear Search ===\n")
    for arr, target, expected in search_tests:
        result = linear_search(arr, target)
        assert result == expected, f"Failed for {arr}, target={target}"
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Found at index: {result}")
        print(" Test passed")
        print("-" * 50)
    
    # Test error handling
    try:
        find_max([])
        assert False, "Expected ValueError for empty list"
    except ValueError:
        print("\nTest passed: Correctly raised ValueError for empty list")
        print(f"Array: {arr}")
        print(f"Searching for: {target}")
        result = linear_search(arr, target)
        if result != -1:
            print(f"Found: {result}")
        else:
            print("Not found")

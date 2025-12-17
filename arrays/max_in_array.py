"""
Problem: Find Maximum Element in Array
Source: Common DSA Problem

Given an array of integers, find the maximum element.

Approach:
1. Initialize the first element as the maximum.
2. Iterate through the array, updating the maximum when a larger element is found.
3. Return the final maximum value.

Time Complexity: O(n) - We need to check each element once
Space Complexity: O(1) - Only constant extra space is used
"""

def find_max(arr):
    """
    Find the maximum element in a list of integers.
    
    Args:
        arr (list): List of integers to find the maximum from
        
    Returns:
        int: The maximum element in the list
        
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

def find_max_builtin(arr):
    """
    Find maximum using Python's built-in max() function.
    This is for comparison and demonstration purposes.
    
    Time Complexity: O(n) - Same as our implementation
    Space Complexity: O(1)
    """
    if not arr:
        raise ValueError("Input list cannot be empty")
    return max(arr)

def linear_search(arr, target):
    """
    Search for a target element in the array.
    
    Args:
        arr (list): List of integers to search in
        target (int): The element to search for
        
    Returns:
        int: The target element if found, otherwise -1
    """
    for num in arr:
        if num == target:
            return num
    return -1

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 5),
        ([1, 3, 2, 5, 4], 5),
        ([42], 42),
        ([-5, -1, -3, -2], -1),
        ([10, 10, 10], 10)
    ]
    
    print("=== Testing Find Maximum ===")
    for nums, expected in test_cases:
        result = find_max(nums)
        print(f"Array: {nums} -> Max: {result}")
        assert result == expected, f"Expected {expected}, got {result}"
    
    # Test empty array case
    try:
        find_max([])
    except ValueError as e:
        print("\nTest passed: Empty array raises ValueError")
    
    # Compare with built-in max
    print("\n=== Comparison with Built-in max() ===")
    for nums, _ in test_cases:
        custom_max = find_max(nums)
        builtin_max = find_max_builtin(nums)
        print(f"Array: {nums} -> Custom: {custom_max}, Built-in: {builtin_max}")
        assert custom_max == builtin_max, "Mismatch with built-in max()"
    
    # Test linear search with specific test cases
    test_cases = [
        ([10, 20, 30, 40, 50], 30),  # Element exists
        ([10, 20, 30, 40, 50], 100), # Element doesn't exist
        ([], 5),                     # Empty array
        ([5], 5),                    # Single element array, target exists
        ([5], 10)                    # Single element array, target doesn't exist
    ]
    
    print("\nTesting Linear Search:")
    print("=" * 30)
    for arr, target in test_cases:
        print(f"Array: {arr}")
        print(f"Searching for: {target}")
        result = linear_search(arr, target)
        if result != -1:
            print(f"Found: {result}")
        else:
            print("Not found")

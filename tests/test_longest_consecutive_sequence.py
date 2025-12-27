import pytest

from arrays.longest_consecutive_sequence import longest_consecutive


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Test case 1: Standard example
        # Input: [100, 4, 200, 1, 3, 2]
        # Sorted: [1, 2, 3, 4, 100, 200]
        # Longest sequence: [1, 2, 3, 4] → length 4
        ([100, 4, 200, 1, 3, 2], 4),
        
        # Test case 2: Unsorted with duplicates
        # Input: [1, 2, 2, 3]
        # Longest sequence: [1, 2, 3] → length 3
        ([1, 2, 2, 3], 3),
        
        # Test case 3: Single element
        # Input: [5]
        # Longest sequence: [5] → length 1
        ([5], 1),
        
        # Test case 4: Empty input
        # Input: []
        # Expected: 0 (no elements)
        ([], 0),
        
        # Test case 5: All identical elements
        # Input: [7, 7, 7]
        # Longest sequence: [7] → length 1
        ([7, 7, 7], 1),
        
        # Test case 6: Negative numbers and mix
        # Input: [0, -1, 1, 2, -2, -3, 3]
        # Sorted: [-3, -2, -1, 0, 1, 2, 3]
        # Longest sequence: [-3, -2, -1, 0, 1, 2, 3] → length 7
        ([0, -1, 1, 2, -2, -3, 3], 7),
        
        # Test case 7: Disjoint sequences
        # Input: [10, 5, 6, 7, 20, 21, 22]
        # Longest sequences: [5,6,7] or [20,21,22] → length 3
        ([10, 5, 6, 7, 20, 21, 22], 3),
        
        # Test case 8: Already consecutive and sorted
        # Input: [1, 2, 3, 4, 5]
        # Longest sequence: [1, 2, 3, 4, 5] → length 5
        ([1, 2, 3, 4, 5], 5),
        
        # Additional edge case: Large gap between sequences
        # Input: [1, 2, 3, 100, 101, 102, 200, 201, 202, 203, 204]
        # Longest sequence: [200, 201, 202, 203, 204] → length 5
        ([1, 2, 3, 100, 101, 102, 200, 201, 202, 203, 204], 5),
    ],
)
def test_longest_consecutive_various_cases(nums, expected):
    assert longest_consecutive(nums) == expected

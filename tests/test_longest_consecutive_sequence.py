import pytest

from arrays.longest_consecutive_sequence import longest_consecutive


@pytest.mark.parametrize(
    "nums, expected",
    [
        # Standard example
        ([100, 4, 200, 1, 3, 2], 4),  # 1,2,3,4
        # Unsorted with duplicates
        ([1, 2, 2, 3], 3),
        # Single element
        ([5], 1),
        # Empty input
        ([], 0),
        # All identical
        ([7, 7, 7], 1),
        # Negative numbers and mix
        ([0, -1, 1, 2, -2, -3, 3], 7),  # -3,-2,-1,0,1,2,3
        # Disjoint sequences
        ([10, 5, 6, 7, 20, 21, 22], 3),  # 5,6,7 or 20,21,22
        # Already consecutive
        ([1, 2, 3, 4, 5], 5),
    ],
)
def test_longest_consecutive_various_cases(nums, expected):
    assert longest_consecutive(nums) == expected

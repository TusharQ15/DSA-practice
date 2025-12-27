import pytest

from arrays.trapping_rain_water import trap


@pytest.mark.parametrize(
    "height, expected",
    [
        # Classic example
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        # Monotonically increasing -> no water
        ([1, 2, 3, 4, 5], 0),
        # Monotonically decreasing -> no water
        ([5, 4, 3, 2, 1], 0),
        # Flat bars -> no water
        ([3, 3, 3, 3], 0),
        # Single pit
        ([3, 0, 2], 2),
        # Multiple pits
        ([4, 2, 0, 3, 2, 5], 9),
        # Too short -> no water
        ([], 0),
        ([1], 0),
        ([1, 2], 0),
        # Large plateau in the middle
        ([2, 0, 2, 0, 2], 4),
    ],
)
def test_trap_various_cases(height, expected):
    assert trap(height) == expected

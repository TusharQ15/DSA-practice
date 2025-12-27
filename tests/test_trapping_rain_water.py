import pytest

from arrays.trapping_rain_water import trap


@pytest.mark.parametrize(
    "height, expected",
    [
        # Test case 1: Classic example
        # Visualization:
        #       X
        #   X   XX X
        # _X_X_XXXXXX
        # 0,1,0,2,1,0,1,3,2,1,2,1
        # Trapped water: 6 units
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        
        # Test case 2: Monotonically increasing -> no water
        # 1,2,3,4,5 (no pits to hold water)
        ([1, 2, 3, 4, 5], 0),
        
        # Test case 3: Monotonically decreasing -> no water
        # 5,4,3,2,1 (no right boundary to hold water)
        ([5, 4, 3, 2, 1], 0),
        
        # Test case 4: Flat terrain -> no water
        # 3,3,3,3 (no variation in height)
        ([3, 3, 3, 3], 0),
        
        # Test case 5: Single pit
        # 3,0,2 (traps 2 units between 3 and 2)
        ([3, 0, 2], 2),
        
        # Test case 6: Multiple pits
        #      X
        # X    X
        # X    X X
        # X  X X X
        # 4,2,0,3,2,5
        # Trapped water: 9 units
        ([4, 2, 0, 3, 2, 5], 9),
        
        # Edge cases:
        ([], 0),      # Empty input
        ([1], 0),     # Single bar
        ([1, 2], 0),  # Two bars (can't trap water)
        
        # Test case 7: Large plateau in the middle
        # X   X
        # X X X
        # 2,0,2,0,2
        # Trapped water: 4 units (1 on each side of middle 0)
        ([2, 0, 2, 0, 2], 4),
    ],
)
def test_trap_various_cases(height, expected):
    assert trap(height) == expected

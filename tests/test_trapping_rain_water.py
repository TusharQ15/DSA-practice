import pytest
from arrays.trapping_rain_water import trap

def test_trap_basic_example():
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

def test_trap_strictly_increasing_returns_zero():
    assert trap([1,2,3,4,5]) == 0

def test_trap_strictly_decreasing_returns_zero():
    assert trap([5,4,3,2,1]) == 0

def test_trap_flat_surface_returns_zero():
    assert trap([0,0,0,0]) == 0
    assert trap([3,3,3,3]) == 0

def test_trap_single_pit():
    assert trap([3,0,3]) == 3
    assert trap([2,0,2]) == 2

def test_trap_multiple_pits():
    assert trap([4,2,0,3,2,5]) == 9

def test_trap_edge_cases():
    assert trap([]) == 0
    assert trap([5]) == 0
    assert trap([5,1]) == 0
    assert trap([5,1,5]) == 4

def test_trap_large_plateau():
    assert trap([2,0,2,0,2]) == 4  # 2 units on each side of middle 0
    assert trap([5,2,1,2,1,5]) == 14  # 4 + 3 + 4 + 3 = 14

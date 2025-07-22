import math
import pytest

# Functions to test
def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(x)

def cube_root(x):
    return x ** (1/3)

def ln(x):
    if x <= 0:
        raise ValueError("Natural log undefined for non-positive values.")
    return math.log(x)

def log10(x):
    if x <= 0:
        raise ValueError("Base-10 log undefined for non-positive values.")
    return math.log10(x)

# Tests for square root
def test_square_root():
    assert round(square_root(4), 4) == 2.0000
    assert round(square_root(0.25), 4) == 0.5000

# Tests for cube root
def test_cube_root():
    assert round(cube_root(8), 4) == 2.0000
    assert round(cube_root(27), 4) == 3.0000

# Tests for natural log
def test_ln():
    assert round(ln(math.e), 4) == 1.0000
    assert round(ln(1), 4) == 0.0000

# Tests for base-10 log
def test_log10():
    assert round(log10(10), 4) == 1.0000
    assert round(log10(100), 4) == 2.0000

# Test for invalid input (negative or zero)
def test_invalid_inputs():
    with pytest.raises(ValueError):
        square_root(-4)
    with pytest.raises(ValueError):
        ln(0)
    with pytest.raises(ValueError):
        log10(-1)

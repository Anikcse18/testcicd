
import pytest
from main import add, subtract, multiply, divide


# ---------- add ----------
def test_add_positive():
    assert add(10, 5) == 15

def test_add_negative():
    assert add(-3, -7) == -10

def test_add_mixed():
    assert add(-5, 5) == 0


# ---------- subtract ----------
def test_subtract_positive():
    assert subtract(10, 5) == 5

def test_subtract_negative_result():
    assert subtract(5, 10) == -5

def test_subtract_zero():
    assert subtract(7, 0) == 7


# ---------- multiply ----------
def test_multiply_positive():
    assert multiply(4, 3) == 12

def test_multiply_by_zero():
    assert multiply(99, 0) == 0

def test_multiply_negatives():
    assert multiply(-2, -3) == 6


# ---------- divide ----------
def test_divide_normal():
    assert divide(10, 5) == 2

def test_divide_float_result():
    assert divide(7, 2) == 3.5

def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
from math_series.series import fibonacci
import pytest

def test_import():
    assert fibonacci
    
def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected
    
def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected
    
def test_fibonacci_seven():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected
    
def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
    

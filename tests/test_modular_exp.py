import pytest
from src.modular_exp import modular_exp  # Replace with the actual module name

def test_basic_cases():
    assert modular_exp(2, 3, 5) == pow(2, 3, 5)
    assert modular_exp(3, 4, 7) == pow(3, 4, 7)
    assert modular_exp(10, 2, 6) == pow(10, 2, 6)

def test_modulus_one():
    assert modular_exp(5, 100, 1) == pow(5, 100, 1)
    assert modular_exp(12345, 67890, 1) == pow(12345, 67890, 1)

def test_large_exponent():
    assert modular_exp(2, 1000, 13) == pow(2, 1000, 13)
    assert modular_exp(5, 500, 97) == pow(5, 500, 97)

def test_base_zero():
    assert modular_exp(0, 5, 7) == pow(0, 5, 7)
    with pytest.raises(ValueError):
        assert modular_exp(0, 0, 5)

def test_exponent_zero():
    assert modular_exp(10, 0, 7) == pow(10, 0, 7)
    with pytest.raises(ValueError):
        assert modular_exp(0, 0, 1)

def test_large_base():
    assert modular_exp(123456789, 2, 1000) == pow(123456789, 2, 1000)

def test_odd_exp():
    base = 9876543210123456789
    exp = 10**5 + 1
    mod = 10**12 + 39
    assert modular_exp(base, exp, mod) == pow(base, exp, mod), "Failed for large odd exponent"

def test_even_exp():
    base = 9876543210123456789
    exp = 10**5
    mod = 10**12 + 39
    assert modular_exp(base, exp, mod) == pow(base, exp, mod), "Failed for large even exponent"

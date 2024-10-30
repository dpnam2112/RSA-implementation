import pytest
from src.prime_generator import PrimeGenerator
from src.prime_checker import PrimeChecker

is_prime = PrimeChecker()
prime_generator = PrimeGenerator(is_prime)

def test_generate_large_prime():
    large_prime = prime_generator(512)
    assert is_prime(large_prime), "Generated number is not prime"
    assert large_prime.bit_length() == 512, "Generated prime does not have the correct bit length"

def test_generate_small_prime():
    small_prime = prime_generator(10)
    assert is_prime(small_prime), "Generated number is not prime"
    assert small_prime.bit_length() <= 10, "Generated prime exceeds bit length"

def test_generate_primes_with_different_bit_counts():
    for bit_count in [8, 16, 32, 64]:
        prime = prime_generator(bit_count)
        assert is_prime(prime), f"Generated number for {bit_count} bits is not prime"
        assert prime.bit_length() == bit_count, f"Generated prime does not have the correct bit length for {bit_count} bits"

def test_invalid_bit_count():
    with pytest.raises(ValueError):
        prime_generator(0)
    with pytest.raises(ValueError):
        prime_generator(-5)

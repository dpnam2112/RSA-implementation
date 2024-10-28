import random
from typing import Callable
from .prime_checker import PrimeChecker

class PrimeGenerator:
    def __init__(self, prime_checker: PrimeChecker | Callable):
        """Generate a prime number.

        Args:
        -  prime_checker: A callable object (like function) used to check if a number is a prime.
        """
        self.prime_checker = prime_checker

    def __call__(self, bit_count: int = 1024) -> int:
        """
        Generate a prime number with the specified bit count.
        :param bit_count: The number of bits for the prime number.
        :return: A prime number with the specified bit count.
        """
        if bit_count < 1:
            raise ValueError("bit_count must be at least 1")

        lower_bound = 1 << (bit_count - 1)  # 2^(bit_count - 1)
        upper_bound = (1 << bit_count) - 1   # 2^bit_count - 1

        while True:
            candidate = random.randint(lower_bound, upper_bound)

            if candidate % 2 == 0 and candidate != 2:
                # All even numbers except 2 are not primes.
                candidate += 1

            if self.prime_checker(candidate):
                return candidate

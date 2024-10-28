import random

from collections.abc import Callable

class PrimeChecker:
    def __init__(self, modular_exp: Callable[[int, int, int], int] = pow):
        """Used to check if a number is a prime.

        Args:
        - modular_exp: If you have a different implementation of modular exponentiation, pass it
          into this parameter. Otherwise, the built-in function `pow` will be used.
        """
        self.modular_exp = modular_exp

    def __call__(self, num: int, iterations: int = 5):
        """Check if number `num` is prime using the Miller-Rabin algorithm."""
        if num <= 1: return False
        if num <= 3: return True # 2 and 3 are primes
        if num % 2 == 0: return False

        exp_base2 = 0
        odd_part = num - 1
        while odd_part % 2 == 0:
            odd_part //= 2
            exp_base2 += 1

        for _ in range(iterations):
            base = random.randint(2, num - 2)  # Random base
            x = self.modular_exp(base, odd_part, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(exp_base2 - 1):
                x = self.modular_exp(x, 2, num)
                if x == num - 1:
                    break
            else:
                return False
        return True

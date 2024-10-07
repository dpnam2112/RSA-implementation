import random

def is_prime(num, iterations=5):
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
        x = pow(base, odd_part, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(exp_base2 - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True

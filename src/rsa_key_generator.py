import random
from .utils import gcd, modular_inverse

def generate_encryption_key(p: int, q: int) -> tuple[int, int]:
    """
    Generate the encryption key (public exponent e) for RSA encryption.
    The public exponent e should be coprime with phiN, where
    phiN = (p - 1) * (q - 1), and 1 < e < phiN.

    Parameters:
    - p (int): A prime number p.
    - q (int): A prime number q.

    Returns:
    - int: The encryption key (public exponent e).
    """
    # Calculate phiN
    phi_n = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phiN and gcd(e, phiN) = 1
    while True:
        e = random.randint(2, phi_n - 1)
        if gcd(e, phi_n) == 1:
            return (p * q, e)

def generate_decryption_key(p: int, q: int, e: int):
    """Generate decryption key, given the generated prime numbers p, q and the encryption key
    e generated from p and q.

    Args:
    - (p, q): the generated prime numbers.
    - e: the encryption key generated from (p, q).

    Returns:
    - tuple: The decryption key, which is a pair of integers.
    """
    # d is modular inverse of e modulo phiN with e and phiN is co prime
    # e * d (mod phiN) = 1 
    phiN = (p - 1) * (q - 1)
    d = modular_inverse(e, phiN)
    return (p * q, d)

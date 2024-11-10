import pytest
from src.prime_checker import PrimeChecker
from src.rsa import RSA
from src.prime_generator import PrimeGenerator

@pytest.fixture
def rsa():
    prime_generator = PrimeGenerator(PrimeChecker())
    return RSA(prime_generator)

def test_encryption_and_decryption(rsa):
    message = 123456
    encrypted_message = rsa.encrypt(message)
    decrypted_message = rsa.decrypt(encrypted_message)
    
    assert decrypted_message == message, f"Expected {message}, but got {decrypted_message}"

def test_encryption_and_decryption_large_numbers(rsa):
    messages = [
        691837477994883320738175066853,
        962171027728358070848901608767,
        363827734347021760832674443167,
        333370850439289180585852421291,
        665203611774036328520408388187,
        387645101065202735028624389873,
        810433571938800504136997667769,
        292377137590078411051280017397,
        466218256180582810978660847543,
        102802689045941268605895235451,
        526466306355103010863983900407
    ]

    for message in messages:
        encrypted_message = rsa.encrypt(message)
        decrypted_message = rsa.decrypt(encrypted_message)
        assert decrypted_message == message, f"Expected {message}, but got {decrypted_message}"

def test_encryption_and_decryption_edge_cases(rsa):
    for message in [0, 1]:
        encrypted_message = rsa.encrypt(message)
        decrypted_message = rsa.decrypt(encrypted_message)
        assert decrypted_message == message, f"Expected {message}, but got {decrypted_message}"

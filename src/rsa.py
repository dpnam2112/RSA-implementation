import json
from typing import Callable
from .prime_generator import PrimeGenerator
from .rsa_key_generator import generate_encryption_key, generate_decryption_key

class RSA:
    def __init__(
        self,
        prime_generator: PrimeGenerator,
        modular_exp: Callable
    ):
        """Initializes the RSA instance with a prime generator and generates the RSA keys.

        Args:
        - prime_generator: A function or class instance that generates prime numbers.
        """
        self.prime_generator = prime_generator
        # p = self.prime_generator()
        # q = self.prime_generator()
        # self.public_key, self.private_key = self._generate_keys(p, q)
        self.modular_exp = modular_exp


    def _generate_keys(self, file_name: str):
        """Generates both the public and private keys for RSA.

        Returns:
        - tuple: The public key (n, e) and private key (n, d).
        """
        p = self.prime_generator()
        q = self.prime_generator()
        n, e = generate_encryption_key(p, q)
        _, d = generate_decryption_key(p, q, e)
        key_pair = {
            "public_key": {
                "n": n,
                "e": e
            },
            "private_key": {
                "n": n,
                "d": d
            }
        }
        with open("text/" + file_name, "w") as json_file:
            json.dump(key_pair, json_file, indent= 4)
        # Return the public and private keys

    def encrypt(self, message: int, e: int, n: int) -> int:
        """Encrypts a message using the public key (n, e).
        
        Args:
        - message: The message to encrypt (as an integer).

        Returns:
        - encrypted_message: The encrypted message as an integer.
        """
        # n, e = self.public_key
        # Encrypt using modular exponentiation
        encrypted_message = self.modular_exp(message, e, n)
        return encrypted_message

    def decrypt(self, encrypted_message: int, d: int, n: int) -> int:
        """Decrypts an encrypted message using the private key (n, d).
        
        Args:
        - encrypted_message: The encrypted message (as an integer).

        Returns:
        - decrypted_message: The decrypted message as an integer.
        """
        # n, d = self.private_key
        # Decrypt using modular exponentiation
        decrypted_message = self.modular_exp(encrypted_message, d, n)
        return decrypted_message

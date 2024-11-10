from .prime_generator import PrimeGenerator
from .rsa_key_generator import generate_encryption_key, generate_decryption_key
from .modular_exp import modular_exp

class RSA:
    def __init__(
        self,
        prime_generator: PrimeGenerator
    ):
        """Initializes the RSA instance with a prime generator and generates the RSA keys.

        Args:
        - prime_generator: A function or class instance that generates prime numbers.
        """
        self.prime_generator = prime_generator
        p = self.prime_generator()
        q = self.prime_generator()
        self.public_key, self.private_key = self._generate_keys(p, q)


    def _generate_keys(self, p, q):
        """Generates both the public and private keys for RSA.

        Returns:
        - tuple: The public key (n, e) and private key (n, d).
        """
        n, e = generate_encryption_key(p, q)
        _, d = generate_decryption_key(p, q, e)
        
        # Return the public and private keys
        return (n, e), (n, d)

    def encrypt(self, message: int) -> int:
        """Encrypts a message using the public key (n, e).
        
        Args:
        - message: The message to encrypt (as an integer).

        Returns:
        - encrypted_message: The encrypted message as an integer.
        """
        n, e = self.public_key
        # Encrypt using modular exponentiation
        encrypted_message = modular_exp(message, e, n)
        return encrypted_message

    def decrypt(self, encrypted_message: int) -> int:
        """Decrypts an encrypted message using the private key (n, d).
        
        Args:
        - encrypted_message: The encrypted message (as an integer).

        Returns:
        - decrypted_message: The decrypted message as an integer.
        """
        n, d = self.private_key
        # Decrypt using modular exponentiation
        decrypted_message = modular_exp(encrypted_message, d, n)
        return decrypted_message

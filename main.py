import sys
import json
from distutils import file_util
from src.modular_exp import modular_exp
from src.prime_checker import PrimeChecker
from src.rsa import RSA
from src.prime_generator import PrimeGenerator

if __name__ == "__main__":
    
    
    if len(sys.argv) < 3 or len(sys.argv) > 5 :
        print("Usage: main.py <status> <file_plaintext> <file_key> <file_output> or <status> <file_cipertext> <file_key> or <status> <file_name>")
        sys.exit(1)

    status = sys.argv[1]
    if len(sys.argv) == 3 :
        # main.py generate_key key.json
        file_name = sys.argv[2]
    else :
        # main.py decrypt encrypted.txt key.json
        file_input = sys.argv[2]
        file_key = sys.argv[3]
        # main.py encrypt plain.txt key.json encrypted.txt
        if len(sys.argv) == 5 :
            file_output = sys.argv[4]
   
    
    modular_exp_callback = modular_exp
    prime_generator = PrimeGenerator(PrimeChecker(modular_exp_callback))
    rsa = RSA(prime_generator, modular_exp)

    if status == 'generate_key':
        rsa._generate_keys(file_name)
        print("Public key and Private Key are saved to", file_name)
        sys.exit(0)
    # Open JSON File to get Key
    with open("text/key.json", "r") as json_file:
        key_pair = json.load(json_file)
    # Encrypt Plaintext
    if status == 'encrypt':
        # Get Public Key by reading JSON File
        public_key = key_pair["public_key"]
        public_n = public_key["n"]
        public_e = public_key["e"]

        # Get Plaintext by reading File input and Write Ciphertext to File ouput
        input = open("text/" + file_input, "r")
        output = open("text/" + file_output, "w")
        m = input.read()
        print("Encrypt Message:", m)
        M = int.from_bytes(m.encode(), byteorder='big')
        c = rsa.encrypt(M, public_e, public_n)
        output.write(str(c))
        print("Encrypted message has been written to", file_output)
        input.close()
        output.close()

    # Decrypt Ciphertext
    if status == 'decrypt':
        # Get Private Key by reading JSON File
        private_key = key_pair["private_key"]
        private_n = private_key["n"]
        private_d = private_key["d"]

        # Get Ciphertext by reading File input and Decrypt Ciphertext
        input = open("text/" + file_input, "r")
        encrypted_msg = rsa.decrypt(int(input.read()), private_d, private_n)
        plaintext_length = (encrypted_msg.bit_length() + 7) // 8
        plaintext = encrypted_msg.to_bytes(plaintext_length, byteorder='big').decode()
        print("Message:", plaintext)
        input.close()

    


    
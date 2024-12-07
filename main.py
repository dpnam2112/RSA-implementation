from pydoc import plainpager
import sys
import json
import argparse
import os
from src.modular_exp import modular_exp
from src.prime_checker import PrimeChecker
from src.rsa import RSA
from src.prime_generator import PrimeGenerator
def is_file_empty(file_path):
    return os.path.exists(file_path) and os.path.getsize(file_path) == 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A command-line tool for RSA')
    sub_parser = parser.add_subparsers(dest = 'command')
    
    # Flag for generate key pair: main.py gen-key-pair -d key.json
    gen_key_parser = sub_parser.add_parser('gen-key-pair', help = 'Generating Key Fair for encrypting and decrypting')
    gen_key_parser.add_argument('-d', '--destination', required=True, help='File to save the key pair (JSON)')
    
    # Flag for Encrypt Plaintext: main.py encrypt --plain plain.txt -k key.json -d encrypted.txt
    encrypt_parser = sub_parser.add_parser('encrypt', help = 'Encrypt Plain text using Public Key')
    encrypt_parser.add_argument('-k', '--key', required=True, help = 'File containing Public Key')
    encrypt_parser.add_argument('--plain', required=True, help='Plain text file to encrypt')
    encrypt_parser.add_argument('-d', '--destination', required=True, help='File to save the encrypted result')
    
    # Flag for Decrypt Ciphertext: main.py decrypt --cipher encrypted.txt  -k key.json
    decrypt_parse = sub_parser.add_parser('decrypt', help = 'Decrypt Ciphertext using Private Key')
    decrypt_parse.add_argument('--cipher', required=True, help = 'File containing Ciphertext')
    decrypt_parse.add_argument('-k', '--key', required=True, help = 'File containing Private Key')
    
    # Initialize RSA
    modular_exp_callback = modular_exp
    prime_generator = PrimeGenerator(PrimeChecker(modular_exp_callback))
    rsa = RSA(prime_generator, modular_exp)

    args = parser.parse_args()
    # Generate Key Pair
    if args.command == 'gen-key-pair':
        rsa._generate_keys(args.destination)
        print("Public key and Private Key are saved to", args.destination)
        sys.exit(0)

    # Encrypt Plaintext
    if args.command == 'encrypt':
        # Open JSON File to get Key
        if is_file_empty("text/" + args.key) :
            rsa._generate_keys(args.key)
        with open("text/" + args.key, "r") as json_file:
            key_pair = json.load(json_file)

        # Get Public Key by reading JSON File
        public_key = key_pair["public_key"]
        public_n = public_key["n"]
        public_e = public_key["e"]

        # Get Plaintext by reading File input and Write Ciphertext to File ouput
        if is_file_empty("text/" + args.plain):
            print("No plaintext to encrypt.")
            sys.exit(1)
        input = open("text/" + args.plain, "r")
        output = open("text/" + args.destination, "w")
        while True:
            m = input.readline().strip()
            if not m:
                break;
            # Convert the string to integer
            M = int.from_bytes(m.encode(), byteorder='big')
            c = rsa.encrypt(M, public_e, public_n)
            output.writelines(str(c) + "\n")
        # m = input.read()
        # print("Encrypt Message:")
        # # Convert the string to integer
        # M = int.from_bytes(m.encode(), byteorder='big')
        # c = rsa.encrypt(M, public_e, public_n)
        # output.write(str(c))
        print("Encrypted message has been written to", args.destination)
        input.close()
        output.close()
    # Decrypt Ciphertext
    if args.command == 'decrypt':
        # Open JSON File to get Key
        if is_file_empty("text/" + args.key) :
            print("No Private Key to Decrypt.")
            sys.exit(1)
        with open("text/" + args.key, "r") as json_file:
            key_pair = json.load(json_file)
        # Get Public Key by reading JSON File
        private_key = key_pair["private_key"]
        private_n = private_key["n"]
        private_d = private_key["d"]
        # Get Ciphertext by reading File input and Decrypt Ciphertext
        if is_file_empty("text/" + args.cipher):
            print("No ciphertext to decrypt.")
            sys.exit(1)
        input = open("text/" + args.cipher, "r")
        print("Message:")
        while True:
            cipherStr = input.readline()
            if not cipherStr:
                break
            encrypted_msg = rsa.decrypt(int(cipherStr), private_d, private_n)
            plaintext_length = (encrypted_msg.bit_length() + 7) // 8
            plaintext = encrypted_msg.to_bytes(plaintext_length, byteorder='big').decode()
            print(plaintext)
        input.close()
    


    


    
import pytest
from src.modular_exp import modular_exp
from src.prime_checker import PrimeChecker
from src.rsa import RSA
from src.prime_generator import PrimeGenerator

@pytest.fixture(scope="module")
def rsa():
    # Use custom function to calculate modular exponentiation instead of using Python's native `pow`.
    modular_exp_callback = modular_exp
    prime_generator = PrimeGenerator(PrimeChecker(modular_exp_callback))
    return RSA(prime_generator, modular_exp)

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

def test_encryption_and_decryption_300_digits_input(rsa):
    messages = [
        336250574371909022718292437556322176382643413103803791977481457656175096265733943709775520785502410670579701257416420397301372312986144507927362320508284350009742419749339766615404060096251075457530294774051782993812714158355480707262356541166559305100718913817306525743740232061025800278355974631903,
        583425925988744464334178583965926274054367288641108033977589008685466583721033751494154078218413687383097032963154747841290668407460115073184834455817755835537584932065639082957404959788642524944439483990479605332332980287085212895798157382376747737051007367700911137727508738224228086904208006060849,
        515494727354779388843358359511470345951433212885428979931717276129426506763181642242088875494297196067302848132403004932830302639652133209400921900327012619645271440591407525213865573442712548199574008940784412998043707624276200296080523061285269213838223518873698711316593181991042523104574362149367,
        468021068222530840519307017931744982146171760400198816352107685247582330130049097475093263973855076888394322139410827804184105101583236451263930187335311900855487991368353130263678594481163806231679421791270202356009005555300884285713896313342501247443127571153662962563862253587603237324945118475067
    ]

    for message in messages:
        encrypted_message = rsa.encrypt(message)
        decrypted_message = rsa.decrypt(encrypted_message)
        assert decrypted_message == message, f"Expected {message}, but got {decrypted_message}"

def test_encryption_and_decryption_random_messages(rsa):
    messages = [
            int.from_bytes(b"Hello world!", byteorder='big'),
            int.from_bytes(b"My name is Harry Potter.", byteorder='big'),
            int.from_bytes(b"Naruto follows the journey of Naruto Uzumaki, a young ninja with dreams of becoming the strongest ninja and earning the title of Hokage, the leader of his village.", byteorder='big'),
            int.from_bytes(b"Harry Potter follows the journey of a young boy who discovers he is a wizard and attends Hogwarts School of Witchcraft and Wizardry", byteorder='big'),
            int.from_bytes(b"Along the way, he confronts dark forces, particularly the dark wizard Voldemort, while forming deep friendships and uncovering secrets about his past.", byteorder='big'),
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

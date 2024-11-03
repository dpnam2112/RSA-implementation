import random
from src.gcd import gcd,ex_gcd
def isCoPrime(p, q):
    return gcd(p, q) == 1

def encryption_key_generate(  p:int, q:int ):
    phiN = (p - 1) * (q - 1)
    e = 2
    randomCo = random.getrandbits(8)
    while e < phiN:
        if isCoPrime(e, phiN):
            if randomCo == 0:
                break
            randomCo -= 1
        e += 1
    return e

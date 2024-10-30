import random

def gcd(p, q) : 
    # find gcd of p and q by using Euclidean Algorithm
    while q:
        p, q = q, p % q
    return p

# egcd(a: int, b: int)
def egcd(a, b) :

    # find x, y satisfy ax + by = gcd(a,b) by using Extended Euclidean Algorithm
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return gcd, x, y
    return old_r, old_s, old_t

def modular_inverse(a, b) :
    # return modular inverse of a modulo b with a and b is co prime
    # a * x (mod b) = 1
    gcd, x, y = egcd(a, b)
    if (x < 0) :
        x += b
    return x

def generate_decryption_key(p, q, e):
    # d is modular inverse of e modulo phiN with e and phiN is co prime
    # e * d (mod phiN) = 1 
    phiN = (p - 1) * (q - 1)
    d = modular_inverse(e, phiN)
    return d

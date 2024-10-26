from prime_generator import is_prime
import random

def gcd(p, q) : 
    while q:
        p, q = q, p % q
    return p

def egcd(a, b) :
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

def modularInverse(a, b) :
    gcd, x, y = egcd(a, b)
    if (x < 0) :
        x += b
    return x

def generator_DecryptionKey(p, q, e):
    phiN = (p - 1) * (q - 1)
    d = modularInverse(e, phiN)
    return d

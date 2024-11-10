def gcd(p, q) : 
    # find gcd of p and q by using Euclidean Algorithm
    while q:
        p, q = q, p % q
    return p

def egcd(a: int, b: int) :
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

def modular_inverse(a: int, b: int) :
    # return modular inverse of a modulo b with a and b is co prime
    # a * x (mod b) = 1
    gcd, x, y = egcd(a, b)
    if (x < 0) :
        x += b
    return x

def modular_exp(base: int, exp: int, mod: int):
    if base < 0 or exp < 0 or mod < 0:
        raise ValueError("Negative parameters are not allowed.")

    if mod == 0:
        raise ValueError("parameter mod cannot be 0.")

    if base == 0 and exp == 0:
        raise ValueError("base and exp cannot both be 0.")

    result = 1
    base = base % mod  # Reduce base if it’s larger than mod

    while exp > 0:
        # If exp is odd, multiply base with the result
        if (exp % 2) == 1:
            result = (result * base) % mod

        # Square the base and reduce exp by half
        exp = exp >> 1  # equivalent to exp // 2
        base = (base * base) % mod

    return result



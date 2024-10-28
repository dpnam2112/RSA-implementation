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

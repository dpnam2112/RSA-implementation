def gcd(a, b):
    """The Euclidean algorithm and returns the gcd of a and b"""    

    while(b != 0 ):
        a, b = b, a%b
    return a

def ex_gcd(a, b):
    """
    Implement the extended Euclidean algorithm (https://cp-algorithms.com/algebra/extended-euclid-algorithm.html).
    This function returns the gcd of a and b, along with the coefficients (x, y) 
    for which a*x + b*y = gcd(a, b)
    Args:
    - a: The first integer.
    - b: The second integer.

    Returns:
    - gcd(a, b): The greatest common divisor of a and b.
    - x: The coefficient for a such that gcd(a, b) = a*x + b*y.
    - y: The coefficient for b such that gcd(a, b) = a*x + b*y.
    """
    x, old_x = 0, 1  
    y, old_y = 1, 0  

    while b != 0:
        quotient = a // b 
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y
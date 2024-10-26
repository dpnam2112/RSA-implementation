from src.gcd import EuclideanAlgorithm
import pytest

def test_gcd():
    # Test case 1: Small numbers
    assert EuclideanAlgorithm.gcd(48, 18) == 6
    assert EuclideanAlgorithm.gcd(56, 98) == 14
    assert EuclideanAlgorithm.gcd(101, 10) == 1  
    assert EuclideanAlgorithm.gcd(0, 5) == 5      # a = 0
    assert EuclideanAlgorithm.gcd(5, 0) == 5     # b = 0

    # Test case 2: Large numbers
    assert EuclideanAlgorithm.gcd(12345678901234567890, 98765432109876543210) == 900000000090
    assert EuclideanAlgorithm.gcd(12345678901234567890, 12345678901234567890) == 12345678901234567890
    assert EuclideanAlgorithm.gcd(1000000000000000000000, 1000000000000000000001) == 1  
    assert EuclideanAlgorithm.gcd(99999999999999999999, 99999999999999999998) == 1   
    assert EuclideanAlgorithm.gcd(1000000000000000000001, 1000000000000000000003) == 1  
    assert EuclideanAlgorithm.gcd(10**18, 10**9) == 10**9   
    assert EuclideanAlgorithm.gcd(10**40, 10**20) == 10**20  
    assert EuclideanAlgorithm.gcd(9999999967, 9999999969) == 1 
    assert EuclideanAlgorithm.gcd(982451653, 982451653) == 982451653  
    assert EuclideanAlgorithm.gcd(982451653, 57885161) == 1 
    assert EuclideanAlgorithm.gcd(32452843, 982451653) == 1  
    assert EuclideanAlgorithm.gcd(2147483647, 2305843009213693951) == 1   
    print("GCD PASSED!")

def test_ex_gcd():
    # Test case 1: Small numbers
    gcd_val, x, y = EuclideanAlgorithm.ex_gcd(48, 18)
    assert gcd_val == 6 and 48 * x + 18 * y == gcd_val, f"Expected GCD(48, 18) = 6, coefficients {x}, {y}"
    
    gcd_val, x, y = EuclideanAlgorithm.ex_gcd(101, 10)
    assert gcd_val == 1 and 101 * x + 10 * y == gcd_val, f"Expected GCD(101, 10) = 1, coefficients {x}, {y}"
    
    gcd_val, x, y = EuclideanAlgorithm.ex_gcd(0, 5)  # a = 0
    assert gcd_val == 5 and 0 * x + 5 * y == gcd_val, f"Expected GCD(0, 5) = 5, coefficients {x}, {y}"
    
    gcd_val, x, y = EuclideanAlgorithm.ex_gcd(5, 0)  # b = 0
    assert gcd_val == 5 and 5 * x + 0 * y == gcd_val, f"Expected GCD(5, 0) = 5, coefficients {x}, {y}"

    # Test case 2: Large numbers
    gcd_val, x, y = EuclideanAlgorithm.ex_gcd(1000000000000000000000, 1000000000000000000001)
    assert gcd_val == 1 and 1000000000000000000000 * x + 1000000000000000000001 * y == gcd_val, f"Expected GCD(1000000000000000000000, 1000000000000000000001) = 1, coefficients {x}, {y}"
    
    gcd_val, x, y = EuclideanAlgorithm.ex_gcd(10**18, 10**9)
    assert gcd_val == 10**9 and 10**18 * x + 10**9 * y == gcd_val, f"Expected GCD(10**18, 10**9) = 10**9, coefficients {x}, {y}"
    
    gcd_val, x, y = EuclideanAlgorithm.ex_gcd(10**40, 10**20)
    assert gcd_val == 10**20 and 10**40 * x + 10**20 * y == gcd_val, f"Expected GCD(10**40, 10**20) = 10**20, coefficients {x}, {y}"
    
    gcd_val, x, y = EuclideanAlgorithm.ex_gcd(9999999967, 9999999969)
    assert gcd_val == 1 and 9999999967 * x + 9999999969 * y == gcd_val, f"Expected GCD(9999999967, 9999999969) = 1, coefficients {x}, {y}"
    
    gcd_val, x, y = EuclideanAlgorithm.ex_gcd(32452843, 982451653)
    assert gcd_val == 1 and 32452843 * x + 982451653 * y == gcd_val, f"Expected GCD(32452843, 982451653) = 1, coefficients {x}, {y}"
    
    gcd_val, x, y = EuclideanAlgorithm.ex_gcd(2147483647, 2305843009213693951)
    assert gcd_val == 1 and 2147483647 * x + 2305843009213693951 * y == gcd_val, f"Expected GCD(2147483647, 2305843009213693951) = 1, coefficients {x}, {y}"
    print("EX_GCD PASSED!")

    
if __name__ == "__main__":
    test_gcd()    
    test_ex_gcd()
    

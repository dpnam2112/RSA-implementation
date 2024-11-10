from src.rsa_key_generator import *

# Result information are taken from https://www.tausquared.net/pages/ctf/rsa.html
def test_generate_decryption_key():
    # Test with some small prime numbers p, q, and e that is co-prime with phiN
    assert(generate_decryption_key(61, 53, 17) == (3233, 2753))
    
    # Test with some small prime numbers p, q, and e that is NOT co-prime with phiN
    # phiN = (61 - 1) * (53 - 1) = 3120, and gcd(3120, 3) = 3 (not co-prime)
    assert(generate_decryption_key(61, 53, 3) != (3233, 2753))
    
    # Test with large prime numbers (100-bit) p, q, and e that is co-prime with phiN
    p_large_100 = 1513157875377811348939992736122821617601
    q_large_100 = 1513157875377811348939992736122821617613
    e_large = 65537
    expected_decryption_key_100 = 799631276182307909905076898457868666799598138929130703395876524607495270582273
    assert(generate_decryption_key(p_large_100, q_large_100, e_large) == (p_large_100 * q_large_100, expected_decryption_key_100))
    
    p_large_100_2 = 1513157875377811348939992736122821617619
    q_large_100_2 = 1513157875377811348939992736122821617631
    expected_decryption_key_100_2 = 871845442901498335008790370544220228087151443869934889190443859395786071411573
    assert(generate_decryption_key(p_large_100_2, q_large_100_2, e_large) == (p_large_100_2 * q_large_100_2, expected_decryption_key_100_2))
    
    # Test with large prime numbers (500-bit) p, q, and e that is co-prime with phiN
    p_large_500 = 21319671980617371648858279800483628024900557635405
    q_large_500 = 21319671980617371648858279800483628024900557635421
    expected_decryption_key_500 = 411306705439390071970085535177974941201652969906881053380771072179072348351845560412745336837918673
    assert(generate_decryption_key(p_large_500, q_large_500, e_large) == (p_large_500 * q_large_500, expected_decryption_key_500))
    
    p_large_500_2 = 21319671980617371648858279800483628024900557635423
    q_large_500_2 = 21319671980617371648858279800483628024900557635429
    expected_decryption_key_500_2 = 119005341179234368854813214705655037789042463715382834010481112644460139558786586842845155914078985
    assert(generate_decryption_key(p_large_500_2, q_large_500_2, e_large) == (p_large_500_2 * q_large_500_2, expected_decryption_key_500_2))
    
    # Test with large prime numbers (1000-bit) p, q, and e that is co-prime with phiN
    p_large_1000 = 151583303970166572396208049746633806491189874688350267668669733400295309378501176489125364961
    q_large_1000 = 151583303970166572396208049746633806491189874688350267668669733400295309378501176489125364973
    expected_decryption_key_1000 = 7956945207666020036969729245764568967909503466444184600988594089271527189992570523555388688029153397605677944219894865811354191846735943956515207430759583271424488638730714540788876673
    assert(generate_decryption_key(p_large_1000, q_large_1000, e_large) == (p_large_1000 * q_large_1000, expected_decryption_key_1000))
    
    p_large_1000 = 151583303970166572396208049746633806491189874688350267668669733400295309378501176489125364979
    q_large_1000 = 151583303970166572396208049746633806491189874688350267668669733400295309378501176489125364991
    expected_decryption_key_1000 = 22955760628858015506525358993894476896844007026456619817128362987224201047136530294328665982482407890159998605727188072443063639075253756440268263236757918943070245604383911545023301973
    assert(generate_decryption_key(p_large_1000, q_large_1000, e_large) == (p_large_1000 * q_large_1000, expected_decryption_key_1000))

def test_generate_encryption_key_with_small_primes():
    # Small primes for testing
    p = 61
    q = 53
    
    n, e = generate_encryption_key(p, q)
    assert n == p * q
    phi_n = (p - 1) * (q - 1)
    assert 1 < e < phi_n
    assert gcd(e, phi_n) == 1

def test_generate_encryption_key_with_another_set_of_primes():
    p = 17
    q = 19
    
    n, e = generate_encryption_key(p, q)
    assert n == p * q
    phi_n = (p - 1) * (q - 1)
    assert 1 < e < phi_n
    assert gcd(e, phi_n) == 1

def test_generate_encryption_key_with_large_primes():
    p = 208756185312071133401043311623
    q = 691837477994883320738175066853
    
    n, e = generate_encryption_key(p, q)
    
    assert n == p * q
    phi_n = (p - 1) * (q - 1)
    assert 1 < e < phi_n

    assert gcd(e, phi_n) == 1

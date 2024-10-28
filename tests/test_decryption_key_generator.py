from src.prime_generator import is_prime
from src.decryption_key_generator import gcd, egcd, modular_inverse, generator_decryption_key

def test_generator_decryption_key():
    # Test with some small prime number p, q and e is co prime with phiN
    assert(generator_decryption_key(61, 53, 17) == 2753)
    # Test with some small prime number p, q and e isn't co prime with phiN
    # phiN = (61 - 1) * (53 - 1) = 3120 and gcd(3120,3) = 3 (is not co prime)
    assert(generator_decryption_key(61, 53, 3) != 2753)
    # Test with some large prime number 100 bit p, q and e is co prime with phiN
    assert(generator_decryption_key(1513157875377811348939992736122821617601, 1513157875377811348939992736122821617613, 65537) == 799631276182307909905076898457868666799598138929130703395876524607495270582273)
    assert(generator_decryption_key(1513157875377811348939992736122821617619, 1513157875377811348939992736122821617631, 65537) == 871845442901498335008790370544220228087151443869934889190443859395786071411573)
    # Test with some large prime number 500 bit p, q and e is co prime with phiN
    assert(generator_decryption_key(21319671980617371648858279800483628024900557635405, 21319671980617371648858279800483628024900557635421, 65537) == 411306705439390071970085535177974941201652969906881053380771072179072348351845560412745336837918673)
    assert(generator_decryption_key(21319671980617371648858279800483628024900557635423, 21319671980617371648858279800483628024900557635429, 65537) == 119005341179234368854813214705655037789042463715382834010481112644460139558786586842845155914078985)
    # # Test with some large prime number 1000 bit p, q and e is co prime with phiN
    assert(generator_decryption_key(151583303970166572396208049746633806491189874688350267668669733400295309378501176489125364961,
                                    151583303970166572396208049746633806491189874688350267668669733400295309378501176489125364973, 65537)
           == 7956945207666020036969729245764568967909503466444184600988594089271527189992570523555388688029153397605677944219894865811354191846735943956515207430759583271424488638730714540788876673)
    assert(generator_decryption_key(151583303970166572396208049746633806491189874688350267668669733400295309378501176489125364979,
                                    151583303970166572396208049746633806491189874688350267668669733400295309378501176489125364991, 65537)
           == 22955760628858015506525358993894476896844007026456619817128362987224201047136530294328665982482407890159998605727188072443063639075253756440268263236757918943070245604383911545023301973)

   
    
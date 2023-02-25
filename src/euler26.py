"""Project Euler #26"""


def mod_pow(b, e, m):
    """Modular exponentiation"""
    if m == 1:
        return 0
    r = 1
    b = b % m
    while e > 0:
        if e % 2 == 1:
            r = (r * b) % m
        b = (b * b) % m
        e = e >> 1
    return r


def fermats_little_theorem(num):
    """Find cyclic numbers using 10**(p-1) = 1 (mod p)"""
    test = 0
    for k in range(1, num):
        rem = mod_pow(10, k, num)
        if rem == 1:
            test = k
            break
    if test == (num - 1):
        return True
    return False


for x in range(1000, 1, -1):
    if fermats_little_theorem(x):
        print(x)
        break

# Wikipedia: cyclic numbers
# Wikipedia: repeating decimals
# Wikipedia: primitive roots
# Wikipedia: fermats little theorem

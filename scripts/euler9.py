"""
euler9.py

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a**2 + b**2 = c**2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagorean_product():
    s = 1000
    for a in range(1, s):
        for b in range(1, a):
            c = s - a - b
            if c ** 2 == a ** 2 + b ** 2:
                print("a:", a, "b:", b, "c:", c)
                print(a * b * c)


pythagorean_product()

from math import factorial


def choose(n, r):
    f = factorial
    return f(n) // f(r) // f(n - r)


print(choose(40, 20))

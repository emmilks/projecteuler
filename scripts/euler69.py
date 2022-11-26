from itertools import accumulate, takewhile
from math import floor, prod, sqrt
from operator import mul

# from project_euler import get_prime_factors

## Naive solution

# def prime_sieve(n):
#     primes = [True] * n
#     primes[0] = False
#     primes[1] = False
#     for p in range(2, floor(sqrt(n)) + 1):
#         if primes[p] == True:
#             for j in range(p * p, n, p):
#                 primes[j] = False
#     return primes


# def totient(n, primes):
#     if n in primes:
#         return n - 1
#     else:
#         pfactors = get_prime_factors(n)
#         inv_pfactors = [(1 - (1 / n)) for n in pfactors]
#         return int(n * prod(inv_pfactors))


# limit = 10 ** 6
# sieve = prime_sieve(limit)
# primes = [prime for prime in range(limit) if sieve[prime]]
# xs = [n / totient(n, primes) for n in range(1, limit + 1)]

# maximum = 0
# maximum_frac = 0
# for i, frac in enumerate(xs):
#     if maximum_frac < frac:
#         maximum_frac = frac
#         maximum = i + 1

# print(maximum)

## Fast solution
def prime_sieve(n):
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    for p in range(2, floor(sqrt(n)) + 1):
        if primes[p] == True:
            for j in range(p * p, n, p):
                primes[j] = False
    return primes


limit = 10 ** 6
sieve = prime_sieve(limit)
primes = [prime for prime in range(limit) if sieve[prime]]
prime_product = list(takewhile(lambda x: x < limit, accumulate(primes, mul)))
print(prime_product[-1])

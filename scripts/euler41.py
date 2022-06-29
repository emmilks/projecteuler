import math


def is_pandigital(n, dig):
    test = "123456789"
    n = "".join(sorted(str(n)))
    return n == test[:dig]


def prime_sieve(n):
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    for p in range(2, math.floor(math.sqrt(n)) + 1):
        if primes[p]:
            for j in range(p * p, n, p):
                primes[j] = False
    return primes


n = 10**8
dig = 7
primes = prime_sieve(n)
max_prime = 0

for i in range(1, dig + 1):
    lower_bound = 10 ** (i - 1) + 1
    upper_bound = 10**i
    for k in range(lower_bound, upper_bound, 2):
        if primes[k] and is_pandigital(k, i) and max_prime < k:
            max_prime = k

print(max_prime)

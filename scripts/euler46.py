from math import floor, sqrt

def prime_sieve(n):
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    for p in range(2,floor(sqrt(n)) + 1):
        if primes[p] == True:
            for j in range(p*p, n, p):
                primes[j] = False
    return primes

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, floor(sqrt(n))+1, 2):
        if n % d == 0:
            return False
    return True

n = 9
while True:
    if not is_prime(n):
        sieve = prime_sieve(n)
        primes = [prime for prime in range(n) if sieve[prime]]
        for prime in primes:
            x = floor(sqrt((n-prime)//2))
            test = prime + 2*x**2
            if test == n:
                break
        if test != n:
            print(n)
            break
    n += 2


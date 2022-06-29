from math import floor, sqrt


def prime_sieve(n):
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    for p in range(2, floor(sqrt(n)) + 1):
        if primes[p] == True:
            for j in range(p * p, n, p):
                primes[j] = False
    return primes


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, floor(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


n = 10**6
sieve = prime_sieve(n)
primes = [prime for prime in range(n) if sieve[prime]]

results = {}
for prime in primes:
    temp = prime
    str_prime = str(prime)
    results.setdefault(prime, [])
    while temp > 0:
        digit = temp % 10
        if digit % 2 == 0 and len(str(prime)) > 1:
            break
        else:
            digit = str(digit)
        temp //= 10
        str_prime = digit + str_prime[:-1]
        if is_prime(int(str_prime)):
            results[prime].append(str_prime)

results = {key: value for key, value in results.items() if len(value) == len(str(key))}

print(len(results))

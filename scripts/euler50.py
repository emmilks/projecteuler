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

n = 10**3
sieve = prime_sieve(n)
primes = [prime for prime in range(n) if sieve[prime]]

max_length = 0
longest = 0

for i in range(len(primes)):
    x = 0
    length = 0
    for j in range(i, len(primes)):
        x += primes[j]
        length += 1
        if x >= n:
            break
        if x in primes and length > max_length:
            max_length = length
            longest = x
print(longest, max_length)

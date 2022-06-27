from math import floor, sqrt
from time import time

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
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, floor(sqrt(n))+1, 2):
        if n % d == 0:
            return False
    return True

start = time()
n = 750000
sieve = prime_sieve(n)
primes = [prime for prime in range(n) if sieve[prime] and prime > 7]
answer = 0

for prime in primes:
    num_prime = 0
    right_trunc = prime
    count = 1
    while right_trunc > 0:
        right_trunc //= 10
        left_trunc = prime % (10**count)
        if is_prime(right_trunc):
            num_prime += 1
        if is_prime(left_trunc):
            num_prime += 1
        count += 1
    if num_prime == 2*count - 3:
        answer += prime

print(answer, round(time() - start,2))

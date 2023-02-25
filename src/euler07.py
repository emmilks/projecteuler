"""
Project_Euler #7
Find the 10,001st prime number
"""
from project_euler import test_primes

primes = []
count = 2
while len(primes) < 10001:
    if test_primes(count):
        primes.append(count)
    count += 1

print(primes[-1])

import math

"""
Project_Euler #10
Find the sum of all the primes below two million.
"""
from project_euler import sieve_eratosthenes

max_int = int(input("Enter maximum integer to test up to: "))
primes = sieve_eratosthenes(max_int)

print(f"Sum of all the prime numbers below {max_int:,}: {sum(primes)}")

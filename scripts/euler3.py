'''
Project_Euler #3
What is the largest prime factor of the number 600851475143?
'''
from project_euler import get_factors, test_primes

test_number = 600851475143
primes = [prime for prime in get_factors(test_number) if test_primes(prime)]

print(f'The largest prime factor of the number {test_number} is: {max(primes)}')

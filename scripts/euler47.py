def num_prime_factors(n):
    factors = set()
    i = 2
    while i*i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return len(factors)

n = 150000
count = 4
for i in range(count+1, n):
        first = num_prime_factors(i-4)
        second = num_prime_factors(i-3)
        third = num_prime_factors(i-2)
        fourth = num_prime_factors(i-1)
        if first == second == third == fourth == count:
            print(i-4)
            break

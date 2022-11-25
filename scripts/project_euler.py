from functools import cache
from itertools import count
from math import ceil, floor, sqrt


def base_conversion(n, base=2):
    """Converts n to a different number base system. Default is binary."""
    converted_number = ""
    hexadecimal = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while n > 0:
        a = n % base
        if base > 10 and a in hexadecimal.keys():
            a = hexadecimal[a]
            converted_number = str(a) + converted_number
            n = n // base
        else:
            converted_number = str(a) + converted_number
            n = n // base

    if converted_number.isdecimal():
        return int(converted_number)
    return converted_number


@cache
def collatz_chain(n):
    """Calculates Collatz sequence for n and returns the length of the sequence"""
    # Collatz Test
    if n == 1:
        return 1
    elif n % 2 == 0:
        chain_size = 1 + collatz_chain(n // 2)
    else:
        chain_size = 2 + collatz_chain((3 * n + 1) // 2)
    return chain_size


def difference_squared_sums(n):
    """Calculates the difference between the sum of the squared natural numbers
    and the square of the sum of the natural numbers"""
    sum = int((n / 2) * (n + 1))
    squared_sum = int((n / 6) * (2 * n + 1) * (n + 1))
    return sum ** 2 - squared_sum


def is_palindrome(x):
    if x < 0:
        return False

    rev_num = 0
    temp = x

    while temp > 0:
        rev_num = rev_num * 10 + (temp % 10)
        temp //= 10

    if rev_num == x:
        return True
    return False


def fibonacci(n):
    """Returns the nth number in the fibonacci sequence."""
    fib1 = 0
    fib2 = 1
    for _ in range(n - 2):
        fib1, fib2 = fib1 + fib2, fib1
    return fib1


def multiple_of_3or5(n):
    """Returns the sum of multiples of 3 or 5 up to the nth number."""
    result = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


def test_primes(n):
    """Determines if the n is prime"""
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    for d in range(3, floor(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def get_factors(n):
    """Finds the factors of the int n and returns a list of the factors"""
    factors = set()
    for d in range(1, floor(sqrt(n)) + 1):
        if n % d == 0:
            factors.add(d)
            factors.add(n // d)
    return factors


def get_prime_factors(n):
    """Finds the factors of the int n and returns a list of the factors"""
    factors = set()
    for d in range(1, floor(sqrt(n)) + 2):
        if n % d == 0 and test_primes(d):
            factors.add(d)
            factors.add(n // d)
    return factors


def anti_prime():
    """Checks if integer is a highly composite number and yields the integers that
    pass the test along with its index."""
    max_div = 0
    for i in count(1):
        div = len(get_factors(i))
        if div > max_div and i != 3:
            max_div = div
            yield (div, i)


def sieve_eratosthenes(limit):
    """Uses the Sieve of Eratosthenes to return a list of
    prime numbers."""

    sievebound = (limit - 1) // 2
    crosslimit = (floor(sqrt(limit)) - 1) // 2
    sieve = [False] * sievebound

    for i in range(1, crosslimit):
        if not sieve[i]:
            for j in range(2 * i * (i + 1), sievebound, 2 * i + 1):
                sieve[j] = True

    yield 2

    for i in range(1, sievebound):
        if not sieve[i]:
            yield 2 * i + 1


def sum_factors(num):
    """Returns sum of the factors of the int n"""
    if num == 1:
        return 1
    n = ceil(sqrt(num))
    total = 1
    divisor = 2
    while divisor < n:
        if num % divisor == 0:
            total += divisor
            total += num // divisor
        divisor += 1
    if n ** 2 == num:
        total += n
    return total


if __name__ == "__main__":
    main()

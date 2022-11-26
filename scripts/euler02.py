"""
Project_Euler # 2
By considering the terms in the Fibonacci sequence whose values do not exceed
4 million, find the sum of the even-valued terms.
"""
from project_euler import fibonacci


def main():
    fib = 0
    index = 0
    even_sum = 0

    # Iterate through fibonacci numbers and add even numbers to even_sum
    while fib <= 4_000_000:
        fib = fibonacci(index)
        if fib % 2 == 0:
            even_sum += fib
        index += 1

    print(f"Even sum: {even_sum}")


main()

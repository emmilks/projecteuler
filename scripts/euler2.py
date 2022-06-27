'''
Project_Euler # 2
By considering the terms in the Fibonacci sequence whose values do not exceed
4 million, find the sum of the even-valued terms.
'''
from project_euler import fibonacci


def main():
    fib = 0
    index = 0
    even_sum = 0
    odd_sum = 0

    while fib <= 4_000_000:
        fib = fibonacci(index)
        if fib % 2 == 0:
            even_sum += fib
        else:
            odd_sum += fib
        index += 1

    print(f"Even sum: {even_sum}")
    print(f"Odd sum: {odd_sum}")


main()

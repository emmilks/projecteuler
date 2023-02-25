"""
euler14.py
Author: Eric Milks

Collatz Conjecture:
    for n > 0:
        if n is even: n/2
        if n is odd: 3n + 1

Find the longest Collatz chain for all numbers less than 1_000_000
"""
from project_euler import collatz_chain

max_number = 1_000_000

print(
    f"This program finds the largest Collatz chain for all numbers less than {max_number:,}.\n"
)
half_max = max_number // 2
longest_chain = 0
answer = 0

for number in range(half_max, max_number):
    if collatz_chain(number) > longest_chain:
        longest_chain = collatz_chain(number)
        answer = number

print(f"Answer: {answer} \nChain size: {longest_chain}")

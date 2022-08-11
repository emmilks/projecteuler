"""
Project_Euler # 4
Find the largest palindrome number made from the product of two 3-digit numbers.
"""
from project_euler import is_palindrome


def solution(min_val=100, max_val=1000):
    max_product = 0
    for i in range(min_val, max_val):
        for j in range(min_val, i):
            if is_palindrome(i * j) and (i * j) > max_product:
                max_product = i * j
    return max_product


print(solution())

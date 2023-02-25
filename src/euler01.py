"""
Project_Euler # 1
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def euler01(n):
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)


n = 1000
answer = euler01(n)
print(answer)

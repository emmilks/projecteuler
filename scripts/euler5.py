'''
Project Euler #5
What is the smallest number divisible by each of the numbers 1 to 20?
'''


def is_divisible(n, max_div):
    for i in range(2, max_div):
        if n % i != 0:
            return False
    return True


n = 20
max_div = 20
while True:
    if is_divisible(n, max_div):
        break
    n += 20

print(n)

from math import factorial

product = factorial(100)

total = 0
while product:
    total += product % 10
    product //= 10
print(total)

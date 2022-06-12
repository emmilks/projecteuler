from math import factorial

digit_factorials = [factorial(i) for i in range(10)]
upper = 7 * factorial(9)
result = 0
for i in range(10, upper + 1):
    number = i
    sum_facts = 0
    while number > 0:
        digit = number % 10
        number //= 10
        sum_facts += digit_factorials[digit]
    if sum_facts == i:
        result += i

print(result)

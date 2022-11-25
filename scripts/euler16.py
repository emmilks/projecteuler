n = 2 ** 1000
total = 0
while n:
    total += n % 10
    n //= 10
print(total)

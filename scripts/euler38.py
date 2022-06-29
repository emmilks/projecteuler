def is_pandigital(n):
    test = "123456789"
    n = "".join(sorted(n))
    return n == test


biggest = 0
for number in range(1, 10000):
    result = ""
    for multiplier in range(1, 10):
        result += str(number * multiplier)
        if is_pandigital(result) and int(result) > biggest:
            biggest = int(result)

print(biggest)

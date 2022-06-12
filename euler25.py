def fibonacci(number):
    fib1 = 1
    fib2 = 1
    for _ in range(number - 2):
        fib1, fib2 = fib1 + fib2, fib1
    return fib1


n = 0
count = 0

while True:
    digit = fibonacci(n)
    while digit != 0:
        digit //= 10
        count += 1

    if count == 1000:
        break
    else:
        count = 0
        n += 1

print(n)

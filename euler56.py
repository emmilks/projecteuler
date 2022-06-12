def digit_sum(x):
    count = 0
    while x > 0:
        count += x % 10
        x //= 10
    return count

answer = 0
for base in range(1,100):
    for power in range(1,100):
        num = digit_sum(base ** power)
        if num > answer:
            answer = num
print(answer)

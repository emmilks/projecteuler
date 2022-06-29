sum = 0
for i in range(1, 1001):
    sum = sum + (i**i)

sum_str = str(sum)
print(sum_str[-10:])

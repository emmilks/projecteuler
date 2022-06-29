result = 0
upper = 9**6
for i in range(2, upper + 1):
    number = i
    sum_fifths = 0
    while number > 0:
        digit = number % 10
        number //= 10
        sum_fifths += digit**5
    if sum_fifths == i:
        result += i
print(result)

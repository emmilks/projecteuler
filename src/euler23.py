from project_euler import sum_factors


def is_abundant(x):
    if sum_factors(x) > x:
        return True
    return False


limit = 28123
abundant_nums = [x for x in range(1, limit + 1) if is_abundant(x)]
sum_abundant_nums = [0] * (limit + 1)

for j in abundant_nums:
    for l in abundant_nums:
        sum1 = j + l
        if sum1 <= limit:
            if sum_abundant_nums[sum1] == 0:
                sum_abundant_nums[sum1] = sum1

total = 0
for x in range(1, len(sum_abundant_nums)):
    if sum_abundant_nums[x] == 0:
        total += x

print(total)

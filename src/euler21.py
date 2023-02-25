from project_euler import get_factors

amicable = []
for i in range(10000):
    factors1 = get_factors(i)[:-1]
    sum_factors = sum(factors1)
    factors2 = get_factors(sum_factors)[:-1]
    sum_factors2 = sum(factors2)

    if sum_factors2 == i and sum_factors2 != sum_factors:
        amicable.append(sum_factors2)

print(sum(amicable))

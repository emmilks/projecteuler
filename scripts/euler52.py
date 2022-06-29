from itertools import permutations

results = {}
for number in range(1, 150001):
    results.setdefault(number, [])
    for multiplier in range(2, 7):
        results[number].append(str(number * multiplier))

for k, v in results.items():
    perms = list(permutations(str(k)))
    perms_list = ["".join(perm) for perm in perms]
    count = 0
    for nums in v:
        if nums in perms_list:
            count += 1
    if count == 5:
        print(k, v)
        break

from itertools import permutations
from math import sqrt, floor

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, floor(sqrt(n))+1, 2):
        if n % d == 0:
            return False
    return True

def is_perm(str1, str2):
    perms = permutations(str1)
    perms_lst = ["".join(perm) for perm in perms]
    if str2 in perms_lst:
        return True
    return False

prime_perms = [p for p in range(1001,10000,2) if is_prime(p)]
diffs = {}
for i in prime_perms:
    for j in prime_perms:
            if abs(j - i) == 3330 and is_perm(str(j), str(i)):
                diffs.setdefault(j, [])
                diffs[j].append(i)
                diffs[j].append(j)

diffs = {key:value for key, value in diffs.items() if len(value) == 4}
for k, v in diffs.items():
    ans = list(map(str, v))
    ans = "".join(ans)
    print(ans[:-4])


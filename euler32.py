from math import sqrt, floor

def is_pandigital(n):
    for i in range(1, floor(sqrt(n)) + 1):
        if n % i == 0:
            temp = str(n) + str(i) + str(n // i)
            if "".join(sorted(temp)) == "123456789":
                return True
    return False

ans = sum(i for i in range(1, 10000) if is_pandigital(i))
print(ans)

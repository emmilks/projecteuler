from itertools import permutations


def test_substring(n):
    tests = [n[1:4], n[2:5], n[3:6], n[4:7], n[5:8], n[6:9], n[7:10]]
    primes = [2, 3, 5, 7, 11, 13, 17]
    xs = zip(primes, tests)
    ys = []
    for prime, test in xs:
        if int(test) % prime == 0:
            ys.append(True)
        else:
            ys.append(False)
    return all(ys)


def get_pandigitals():
    perms = permutations("0123456789")
    return ["".join(perm) for perm in perms]


pandigitals = get_pandigitals()
answer = sum(int(n) for n in pandigitals if test_substring(n))
print(answer)

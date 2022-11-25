from collections import Counter

s = 1000
lst = []
for a in range(3, (s - 3) // 3 + 1):
    for b in range(a + 1, (s - 1 - a) // 2 + 1):
        c = (a ** 2 + b ** 2) ** 0.5
        p = a + b + c
        if p <= 1000:
            lst.append(p)
c = Counter(lst)
print(int(c.most_common(1)[0][0]))

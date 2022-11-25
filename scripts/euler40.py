max_n = 1000000
s = ""
for i in range(1, max_n + 1):
    s += str(i)

d = 1
n = 0
for i, j in enumerate(s):
    k = i + 1
    if k == 10 ** n:
        d *= int(j)
        n += 1

print(n)
print(d)

from math import floor, log

answer = 0
for n in range(1, 10):
    answer += floor(log(10, 10 / n))
print(answer)

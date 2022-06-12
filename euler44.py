def pentagonal(n):
    return n * (3*n-1) // 2

LIMIT = 2500
pentagonals = [pentagonal(n) for n in range(1,LIMIT+1)]
possibles = []
for i in pentagonals:
    for j in pentagonals:
        add = i + j
        sub = i - j
        if add in pentagonals and abs(sub) in pentagonals:
            possibles.append(abs(sub))
            print(abs(sub))
    if len(possibles) > 0:
        break

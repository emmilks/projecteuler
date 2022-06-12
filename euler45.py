def triangle_num(n):
    return n * (n + 1) // 2


def pentagonal_num(n):
    return n * (3 * n - 1) // 2


def hexagonal_num(n):
    return n * (2 * n - 1)


t_set = set(triangle_num(t) for t in range(286, 100001))
p_set = set(pentagonal_num(p) for p in range(166, 100001))
h_set = set(hexagonal_num(h) for h in range(144, 100001))

print(t_set & p_set & h_set)

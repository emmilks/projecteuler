import itertools

digits = "0123456789"
perms = list(itertools.permutations(digits))
perms_list = ["".join(perm) for perm in perms]

perms_list = sorted(perms_list)
print(perms_list[999999])

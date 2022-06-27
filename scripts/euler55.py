def is_palindrome(x):
    if x < 0:
        return False

    rev_num = 0
    temp = x
    
    while temp > 0:
        rev_num = rev_num*10 + (temp % 10)
        temp //= 10
        
    if rev_num == x:
        return True
    return False

def reverse_number(x):
    rev_num = 0
    temp = x
    
    while temp > 0:
        rev_num = rev_num*10 + (temp % 10)
        temp //= 10
    return rev_num

def is_lychrel(x):
    for _ in range(50):
        num = x + reverse_number(x)
        if is_palindrome(num):
            return False
        else:
            x = num
    return True

answer = 0
for i in range(10000):
    if is_lychrel(i):
        answer += 1
print(answer)

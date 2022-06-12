from project_euler import is_palindrome, base_conversion

palindrome = []
for i in range(1, 1_000_001):
    if is_palindrome(i) and is_palindrome(base_conversion(i)):
        palindrome.append(i)

answer = sum(palindrome)
print(answer)

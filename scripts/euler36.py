from project_euler import base_conversion, is_palindrome

palindrome = []
for i in range(1, 1_000_001):
    if is_palindrome(i) and is_palindrome(base_conversion(i)):
        palindrome.append(i)

answer = sum(palindrome)
print(answer)

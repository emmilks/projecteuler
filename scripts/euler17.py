from num2words import num2words


def number_letter_count(num):
    return sum(1 for l in num2words(num) if l.isalpha())


print(sum(number_letter_count(i) for i in range(1, 1001)))

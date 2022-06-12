"""
Project Euler 42

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value. For example, the word value for
SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall
call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing
nearly two-thousand common English words, how many are triangle words?
"""


def is_triangle_number(n, triangle_nums):
    """Returns True if n is a triangle number"""
    if n in triangle_nums:
        return True
    return False


def get_triangle_numbers(n):
    """Returns nth triangle number"""
    return (n * (n + 1)) // 2


def letter_value(let):
    """Converts letter to ASCII code and returns position in alphabet"""
    return ord(let) - 64


# Arbitrarily long list of triangle numbers to compare
triangle_numbers = [get_triangle_numbers(n) for n in range(1, 19)]
triangle_word = 0

with open("euler42.txt", 'r') as f:
    # Breaks down file to read each individual character
    for line in f:
        delim = line.strip().split(',')
        for word in delim:
            word_value = 0
            for letter in word:
                # Checks if character is a letter and adds letter value
                # to word_value if true
                if letter.isalpha():
                    word_value += letter_value(letter)
            # Checks if current word_value is a triangle number and
            # iterates triangle_word if true
            if is_triangle_number(word_value, triangle_numbers):
                triangle_word += 1

print(triangle_word)

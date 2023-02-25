def letter_value(let):
    return ord(let) - 64


with open("../data/euler22.txt", "r") as f:
    names = sorted([line.replace('"', "") for line in f.read().strip().split(",")])

name_score = 0
for i, name in enumerate(names):
    word_value = 0
    for letter in name:
        word_value += letter_value(letter)
    name_score += word_value * (i + 1)

print(name_score)

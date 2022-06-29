def max_max_path(mat):
    for i in range(len(mat) - 2, -1, -1):
        for j in range(i + 1):
            mat[i][j] += max(mat[i + 1][j], mat[i + 1][j + 1])
    return mat[0][0]


with open("../data/euler18.txt", "r") as file:
    matrix = [line.strip().split() for line in file]

for j in range(len(matrix)):
    matrix[j] = list(map(int, matrix[j]))
print(max_max_path(matrix))

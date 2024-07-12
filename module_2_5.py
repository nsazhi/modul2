def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = [] * n
        matrix.append(row)
        for j in range(m):
            row.append(value)
    return matrix

n = 3
m = 4
value = 25
matrix = get_matrix(n, m, value)
print(matrix)
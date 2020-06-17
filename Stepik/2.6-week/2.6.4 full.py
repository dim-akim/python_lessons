matrix = []
while True:
    a = input()
    if a == 'end':
        break
    else:
        matrix.append([int(i) for i in a.split()])

result = []

for i in range(len(matrix)):
    row = []
    for j in range(len(matrix[i])):
        row.append(matrix[i+1-len(matrix)][j] +
                   matrix[i-1][j] +
                   matrix[i][j+1-len(matrix[i])] +
                   matrix[i][j-1])
    result.append(row)

for i in range(len(result)):
    print(*result[i])

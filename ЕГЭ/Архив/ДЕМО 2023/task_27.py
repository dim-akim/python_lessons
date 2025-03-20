with open('27-B.txt') as file:
    n = int(file.readline())
    matrix = [[0] * 9 for _ in range(9)]
    answer = 0

    for pos in range(n):
        a = int(file.readline())
        for row in range(9):
            answer += matrix[row][(pos - a - row) % 9]
        matrix[a % 9][pos % 9] += 1


print(*matrix, sep='\n')
print(f'{a=} {answer=}')
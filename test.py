def div_count(n, divisor):
    count = 0
    while n % divisor == 0:
        n //= divisor
        count += 1
    return count


with open('27-B.txt') as file:
    n = int(file.readline())
    numbers = [int(line) for line in file]


matrix_2_5 = [[0 for i in range(9)] for j in range(9)]
# 2 по горизонтали, 5 по вертикали

for number in numbers:
    div_2 = div_count(number, 2)
    if div_2 > 7:
        div_2 = 8
    div_5 = div_count(number, 5)
    if div_5 > 7:
        div_5 = 8

    matrix_2_5[div_5][div_2] += 1

# cnt = 0
# for number in numbers:
#     if div_count(number, 2) == 1 and div_count(number, 5) == 0:
#         cnt += 1

# print(cnt)
for line in matrix_2_5:
    print(line)

cnt = 0
# i - 5, j - 2
for i in range(9):
    for j in range(9):
        for k in range(9):
            for m in range(9):
                if i + k >= 7 and j + m == 7 or i + k == 7 and j + m >= 7:
                    cnt += matrix_2_5[i][j] * matrix_2_5[k][m]

print(cnt / 2)

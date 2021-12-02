n = 6
a = [2, 8, 15, 6, -5, 3]

b = []
for i in range(n):
    # ищем минимальное значение в массиве
    minimum = a[0]
    for j in range(n):
        if a[j] < minimum:
            minimum = a[j]

    b.append(minimum)
    a.remove(minimum)
    n = n - 1    # решаем проблему с изменением длины списка

print(b)

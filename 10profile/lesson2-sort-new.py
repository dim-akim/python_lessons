n = ввод
a = ввод

b = []
for i in range(6):
    minimum = a[0]
    for j in range(n):
        if a[j] < minimum:
            minimum = a[j]
    b.append(minimum)
    a.remove(minimum)

print(b)

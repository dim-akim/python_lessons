a = [1, 5, 3, 8, 4, 9]

n = len(a)
for i in range(n):
    min = a[i]
    min_j = i
    for j in range(i + 1, n):
        if a[j] < min:
            min = a[j]
            min_j = j
    a[i], a[min_j] = a[min_j], a[i]

print(a)

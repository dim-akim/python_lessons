n = 6
a = [8, 4, 15, 8, 9, 4]

minimum = a[0]
for i in range(1, n):
    if a[i] < minimum:
        minimum = a[i]

print(minimum)

n = 6
a = [2, 8, 15, 6, -5, 3]

start_index = 0
for i in range(n):

    min_index = start_index
    for j in range(start_index, n):
        if a[j] < a[min_index]:
            min_index = j

    # temp = a[start_index]
    # a[start_index] = a[min_index]
    # a[min_index] = temp

    a[start_index], a[min_index] = a[min_index], a[start_index]

    start_index += 1

print(a)

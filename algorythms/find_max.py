import timeit


def list_append():
    n = 7
    a = []
    a.append(1)
    a.append(3)
    a.append(8)
    a.append(5)
    a.append(4)
    a.append(7)
    a.append(3)
    max_a = a[0]
    for i in range(1, n):
        if a[i] > max_a:
            max_a = a[i]
    print(max_a)


def list_create():
    n = 7
    a = [0] * 7
    a[0] = 1
    a[1] = 3
    a[2] = 8
    a[3] = 5
    a[4] = 4
    a[5] = 7
    a[6] = 3
    max_a = a[0]
    for i in range(1, n):
        if a[i] > max_a:
            max_a = a[i]
    print(max_a)


time1 = timeit.timeit(list_append, number=10000)
time2 = timeit.timeit(list_create, number=10000)
print(time1)
print(time2)

import timeit


def evklid2():
    a = 22
    b = 8
    while b:
        a, b = b, a % b
    print(b)


def evklid():
    a = 22
    b = 8

    while b != 0:
        c = a % b
        a = b
        b = c

    print(a)


def simple_nod():
    a = 22
    b = 8

    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            nod = i
            break

    print(nod)


time1 = timeit.timeit(simple_nod, number=10000)
time2 = timeit.timeit(evklid, number=10000)
time3 = timeit.timeit(evklid2, number=10000)
print(time1)
print(time2)
print(time3)

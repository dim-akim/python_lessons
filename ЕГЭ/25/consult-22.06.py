def is_simple(n):
    for d in range(int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


for x in range(45000000, 50000001):
    k = 0
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0:
            if d % 2 != 0:
                k += 1
            if x // d == d:
                continue
            elif (x // d) % 2 != 0:
                k += 1

    if k == 5:
        print(x)

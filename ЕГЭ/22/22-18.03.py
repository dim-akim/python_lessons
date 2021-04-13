for i in range(1, 1000):
    x = i
    k = x % 9
    a = 0
    b = 0
    while x > 0:
        d = x % 9
        if d == k:
            a += 1
        b += d
        x //= 9
    if a == 3 and b == 10:
        print(f'{i=} {a=} {b=}')

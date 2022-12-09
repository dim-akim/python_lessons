for x in range(101, 200):
    L = x
    M = 65

    if L % 2 == 0:
        M = 52

    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    print(f'{x=} {M=}')

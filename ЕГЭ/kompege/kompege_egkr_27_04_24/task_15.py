for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        f = (x % A > 0) <= ((x % 28 == 0) <= (x % 49 > 0))
        if not f:
            flag = False
            break

    if flag:
        print(A)

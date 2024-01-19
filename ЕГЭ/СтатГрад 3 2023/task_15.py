for A in range(1, 100):
    flag = True
    for x in range(1, 10000):
        if (((x&35 != 0) or (x&22 != 0)) <= ((x&15 == 0) <= (x&A != 0))) == 0:
            flag = False
            break

    if flag:
        print(f'{A=}')

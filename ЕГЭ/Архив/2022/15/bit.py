for A in range(1, 100):
    flag = 0
    for x in range(1, 10000):
        if (((x & 77) != 0) <= (((x & 12) == 0) <= ((x & A) != 0))) is False:
            flag = 1
            break
    if flag == 0:
        print(A)

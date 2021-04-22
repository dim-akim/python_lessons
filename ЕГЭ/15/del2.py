for A in range(1, 1000):
    flag = 0
    for x in range(1, 1000):
        if ((A % 40 == 0) and ((780 % x == 0) <= ((A % x != 0) <= (180 % x != 0)))) is False:
            flag = 1
            break
    if not flag:
        print(A)

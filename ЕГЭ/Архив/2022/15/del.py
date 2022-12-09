for A in range(1, 200):
    flag = 0
    for x in range(1, 10000):
        if (A % 45 == 0 and ((750 % x == 0) <= ((A % x != 0) <= (120 % x != 0)))) is False:
            flag = 1
            break
    if not flag:
        print(A)

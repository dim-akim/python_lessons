# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)

for A in range(0, 1000):
    # flag = True
    for x in range(1, 10000):
        if ((x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))) != 1:
            # flag = False
            break
    else:
        print(A)
        break
    # if flag:
    #     print(A)

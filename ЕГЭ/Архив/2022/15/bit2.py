# x&33=0 <= (x&45 != 0 <= x&A != 0)

for A in range(100):
    flag = 0
    for x in range(1, 1000):
        if (((x & 33) == 0) <= (((x & 45) != 0) <= ((x & A) != 0))) == 0:
            flag = 1
            break
    if not flag:
        print(A)

# (3*x + y > A) and (y < x) and (x < 30)

for A in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            f = (3*x + y > A) and (y < x) and (x < 30)
            if f:
                flag = False
                break
        if not flag:
            break

    if flag:
        print(A)

def triangle_exists(n, m, k):
    return n + m > k and m + k > n and n + k > m


for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        impres = not((triangle_exists(x, 11, 18) == (not (max(x, 5) > 68))) and triangle_exists(x, A, 5))
        if impres is False:
            flag = False
            break

    if flag:
        print(f'{A=}')

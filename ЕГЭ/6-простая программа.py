for i in range(300):
    s = i
    s = 10 * s + 7
    n = 1
    while s < 2021:
        s = s + 2 * n
        n = n + 1
    if n == 13:
        print(i)
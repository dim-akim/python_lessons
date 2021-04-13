def F(n):
    if n == 0:
        return 0
    elif n % 3 == 0:
        return F(n // 3)
    else:
        return n % 3 + F(n - n % 3)


for n in range(1, 1000):
    if F(n) == 11:
        print(n)
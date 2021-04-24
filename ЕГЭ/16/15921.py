def F(n):
    if n > 0:
        print(n)
        F(n - 4)
        F(n // 2)


print(F(9))

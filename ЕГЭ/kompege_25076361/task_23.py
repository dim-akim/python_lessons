def f(a, b, has20 = False):
    if a == b:
        return 1
    if a > b or a == 30 and has20:
        return 0
    if a == 20:
        has20 = True
    return f(a + 2, b, has20) + f(a + 3, b, has20) + f(a * 2, b, has20)


print(f(8, 35))

def f(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    if a == 16:
        return 0
    return f(a + 1, b) + f(a + 3, b) + f(a ** 2, b)


print(f(3, 20) * f(20, 26))

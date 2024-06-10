def f1(a: int, b: int) -> int:
    if a == b:
        return 1
    if a > b:
        return 0
    return f1(a + 1, b) + f1(a + 3, b) + f1(a * 2, b)


def f3(a: int, b: int) -> int:
    if a == b:
        return 1
    if a > b:
        return 0
    return f3(a + 2, b) + f3(a + 4, b)


print(1, f1(3, 12) * f1(12, 16))
print(3, f3(4, 15))

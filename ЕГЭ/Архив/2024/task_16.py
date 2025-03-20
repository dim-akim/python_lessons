"""
F(n)=n, если n≥2025,
F(n)=n+3+F(n+3), если n<2025.

Чему равно значение выражения F(23)−F(21)?
"""


def f(n):
    if n >= 2025:
        return n
    return n + 3 + f(n+3)


f_list = [0] * 2025 + [2025, 2026, 2027]


def f2(n):
    if n < 2025:
        for i in range(2024, n - 1, -1):
            f_list[i] = i + 3 + f2(i+3)
            print(f'{i=} {f_list[i]=}')
    return f_list[n]


print(f(23) - f(21))
print(f2(23) - f2(21))

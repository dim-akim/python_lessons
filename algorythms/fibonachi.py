def fib(n: int) -> int:
    """
    Возвращает n-ное число Фибоначчи. Реализация с помощью рекурсии
    """
    if n <= 1:  # n >= 0
        return n
    return fib(n-1) + fib(n-2)


def fib2(n: int) -> int:
    """
    Возвращает n-ное число Фибоначчи. Реализация с помощью динамического программирования
    """
    if n >= len(fib_list):
        a = fib2(n-1) + fib2(n-2)
        fib_list.append(a)
    return fib_list[n]


def fib3(n: int) -> int:
    fibonachi = [0, 1]
    for i in range(2, n + 1):
        fibonachi.append(fibonachi[i-1] + fibonachi[i-2])
    return fibonachi[n]


fib_list = [0, 1]

print(fib3(100))
print(fib2(100))
print(fib2(80))
print(fib(10))
print(fib_list)

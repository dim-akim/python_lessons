def matryoshka(n):
    print('Верхняя часть матрешки уровня', n)
    if n > 1:  # рекуррентный случай
        matryoshka(n-1)
    print('Нижняя часть матрешки уровня', n)


def fact(n: int) -> int:
    if n <= 1:  # крайний случай
        return 1
    return n * fact(n-1)  # рекуррентный случай


def fib(n: int) -> int:
    if n <= 1:  # крайний случай
        return n
    return fib(n-2) + fib(n-1)  # рекуррентный случай


# Фибоначчи с запоминанием промежуточных результатов
fib_list = [0, 1]


def fib_with_mem(n):
    if n < len(fib_list):
        return fib_list[n]
    for i in range(len(fib_list), n+1):
        fib_list.append(fib_list[i-2] + fib_list[i-1])
    return fib_list[n]


# for i in range(100 + 1):
#     # print(i, fib(i))
#     print(i, fib_with_mem(i))


def gcd(a: int, b: int) -> int:
    print(a, b)  # отладочная печать
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    return gcd(b-a, a)


print(gcd(2700, 6))

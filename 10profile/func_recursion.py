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


def gcd2(a: int, b: int) -> int:
    print(a, b)  # отладочная печать
    if b == 0:
        return a

    return gcd2(b, a % b)


def gcd3(a: int, b: int) -> int:
    return a if b == 0 else gcd3(b, a % b)


def pow(a: int, b: int) -> int:
    print(a, b)
    if b == 0:
        return 1
    # условие-призрак b != 0
    return a * pow(a, b-1)


def pow2(a: int, b: int) -> int:
    """
    Быстро возводит число a в степень b.
    Для четных b используется оптимизирующий прием
    :param a:
    :param b:
    :return:
    """
    print(a, b)
    if b == 0:
        return 1
    elif b % 2 > 0:
        return a * pow2(a, b-1)
    return pow2(a*a, b // 2)


print(pow2(2, 10))

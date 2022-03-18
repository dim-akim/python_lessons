def matryoshka(n: int) -> None:  # n = ГЛУБИНА рекурсии
    """
    Выводит в консоль TODO дописать документ-строку
    """
    print(f'Верх матрёшки {n=}')  # ПРЯМОЙ ход рекурсии
    if n > 1:  # РЕКУРРЕНТНЫЙ случай
        matryoshka(n-1)  # вызов функции с УПРОЩЕННЫМИ данными
    print(f'Низ матрёшки {n=}')  # ОБРАТНЫЙ ход рекурсии


def fact(n: int) -> int:
    """
    Возвращает факториал от числа n
    """
    if n <= 1:
        return 1
    return fact(n-1) * n


def gcd(a: int, b: int) -> int:
    """
    Возвращает Наибольший Общий Делитель чисел a и b, вычисленный по алгоритму Евклида
    """
    # if b == 0:
    #     return a
    # # условие-призрак: b != 0
    # return gcd(b, a % b)
    # return a if not b else gcd(b, a % b)
    return gcd(b, a % b) if b else a


def power(a: float, n: int) -> float:
    """
    Возводит число a в натуральную степень n
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a * a, n // 2)
    # условие призрак: n % 2 != 0
    return power(a, n-1) * a


def generate_numbers(n: int, m: int, prefix=None) -> None:
    """
    Выводит в консоль все числа длиной m в системе счисления n
    """
    if m == 0:
        print(*prefix)
        return
    prefix = prefix or []
    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m-1, prefix)
        prefix.pop()


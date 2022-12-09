from one_way_algo import is_prime
from one_way_algo import find_simple_numbers


def factorize(n: int):
    """
    Выводит на экран все простые делители числа n в строчку
    :param n: Целое положительное число
    """
    for divisor in range(2, n+1):
        if n % divisor == 0 and is_prime(divisor):
            print(divisor, end=' ')
    print()


factorize(6)  # 2 3
factorize(8)  # 2
factorize(75)  # 3 5

def is_prime(n: int) -> bool:
    """
    Проверяет, простое число или нет.
    :param n: натуральное число.
    :return: True если число простое.
    """
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_simple_numbers(n: int) -> None:
    """
    Находит и распечатыает простые числа в диапазоне от 1 до n включительно
    :param n: правая граница искомого диапазона
    """
    for number in range(1, n+1):
        if is_prime(number):
            print(number, end=' ')


print(__name__)
if __name__ == '__main__':
    a = 31
    print(is_prime(31))
    print(is_prime(300))
    print(is_prime(2))

    find_simple_numbers(100)

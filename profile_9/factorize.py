# import profile_9.BruteForce
# import profile_9.BruteForce as bf
from profile_9.BruteForce import is_simple


def factorize(n):
    """
    Функция выводит на экран простые делители, каждый в новой строке
    :param n: целое число больше 2
    :return: None
    """
    # Проверка ввода
    if type(n) is not int:
        print('Получено не число')
        return
    elif n < 2:
        print('Число должно быть больше 2')
        return
    for divisor in range(2, n):
        if is_simple(divisor) and n % divisor == 0:
            print(divisor)


if __name__ == '__main__':
    factorize('456')

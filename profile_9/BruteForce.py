def is_simple(n):
    divisor = 2
    while divisor ** 2 <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


if __name__ == '__main__':
    for number in range(1, 1000):
        if is_simple(number):
            print(number)

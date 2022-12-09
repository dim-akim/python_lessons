def is_simple(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def f(n):
    k = 0
    for divisor in range(2, int(n**0.5)):
        if n % divisor == 0:
            if is_simple(divisor):
                k += 1
            if is_simple(n // divisor):
                k += 1
            if k > 3:
                break
    divisor += 1
    if n == divisor ** 2:
        if is_simple(divisor):
            k += 1
    return k


minimum = 50001
count = 0
for number in range(10001, 50001):

    if f(number) == 3:
        count += 1
        if number < minimum:
            minimum = number

print(count, minimum)

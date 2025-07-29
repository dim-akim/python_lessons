# def is_prime(number):
#     if number % 2 == 0 and number != 2:
#         return False
#     for i in range(3, int(number**.5) + 1, 2):
#         if number % i == 0:
#             return False
#     return True
#
#
# def r(n):
#     divisors = set()
#     for i in range(2, int(n**.5) + 1):
#         if n % i == 0:
#             divisors.add(i)
#             divisors.add(n // i)
#     return sum(divisors)
#
#
# count = 0
# for i in range(500_000, 500_000_000):
#     if r(i) % 10 == 9:
#         count += 1
#         print(f'{i=} {r(i)=}')
#     if count == 5:
#         break
# for i in range(1, 100):
#     if is_prime(i):
#         print(i)
def prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def divisor(x):
    divisors = set()
    for o in range(2, int(x**.5) + 1):
        if x % o == 0:
            if prime(o):
                divisors.add(o)
            if prime(x // o):
                divisors.add((x // o))
    return sorted(divisors)


for i in range(456790, 460000):
    f = divisor(i)
    if f:
        if len(f) >= 4:
            M = f[0] + f[1] + f[-1] + f[-2]
            if M % 114 == 39:
                print(i, M)

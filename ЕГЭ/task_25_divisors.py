def is_prime(number):
    if number % 2 == 0 and number != 2:
        return False
    for i in range(3, int(number**.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def r(n):
    divisors = set()
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sum(divisors)


# count = 0
# for i in range(500_000, 500_000_000):
#     if r(i) % 10 == 9:
#         count += 1
#         print(f'{i=} {r(i)=}')
#     if count == 5:
#         break
for i in range(1, 100):
    if is_prime(i):
        print(i)

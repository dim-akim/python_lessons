def r(n):
    number = [int(i) for i in str(n)]
    sum_even = sum(i for i in number if i % 2 == 0)
    dif = max(number) - min(number)
    a = sum_even ** 2
    b = dif ** 3
    if a >= b:
        return int(f'{b}{a}')
    return int(f'{a}{b}')


for i in range(1000, 10000):
    if r(i) == 4343:
        print(i)

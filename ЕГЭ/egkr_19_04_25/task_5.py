def to3(n):
    ans = ''
    while n:
        ans = str(n % 3) + ans
        n //= 3
    return ans


for n in range(3, 1000):
    n3 = to3(n)
    if n3[-1] == '0':
        n3 = n3 + n3[-2:]
    else:
        n3 += to3((n % 3) * 3)
    r = int(n3, 3)
    if r <= 150:
        print(f'{n=} {n3=} {r=}')

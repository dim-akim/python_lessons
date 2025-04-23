def to_7(n):
    ans = ''
    while n:
        ans = str(n % 7) + ans
        n //= 7
    return ans


result = []
for n in range(100, 100000):
    n7 = to_7(n)
    if n7.count('3') % 2 == 0:
        n7 = '3' + n7 + n7[0]
    else:
        n7 = '6' + n7 + n7[-1]
    r = int(n7, 7)
    print(f'{n=} {n7=} {r=}')

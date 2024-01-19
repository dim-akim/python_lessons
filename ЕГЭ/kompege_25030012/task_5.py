def to_6(n):
    result = ''
    while n:
        result += str(n % 6)
        n //= 6
    return result[::-1]


r_list = []
for n in range(1, 1000):

    n_6 = to_6(n)
    if n % 3 == 0:
        n_6 += n_6[:2]
    else:
        ost = n % 3 * 10
        n_6 += to_6(ost)
    r = int(n_6, 6)
    if r > 680:
        r_list.append((r, n))

    print(f'{n=} {r=}')
print(min(r_list))

for i in range(1, 1000):
    n = i
    n2 = bin(n)[2:]
    if n2.count('1') % 2 == 0:
        n2 += '0'
        n2 = '10' + n2[2:]
    else:
        n2 += '1'
        n2 = '11' + n2[2:]
    r = int(n2, base=2)
    if r == 40:
        print(f'{n=} {r=}')


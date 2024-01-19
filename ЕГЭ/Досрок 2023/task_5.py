for i in range(1, 100):
    n = i
    n2 = bin(n)[2:]
    if n % 3 == 0:
        # n2 += n2[-3] + n2[-2] + n2[-1]
        n2 += n2[-3:]
    else:
        ost = n % 3 * 3
        n2 += bin(ost)[2:]
    r = int(n2, base=2)
    if r >= 76:
        print(f'{n=} {r=}')
        break

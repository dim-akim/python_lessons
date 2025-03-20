for n in range(1, 1000):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n += bin_n[-2:]
    else:
        bin_n = '1' + bin_n + '0'
    r = int(bin_n, 2)
    if r < 100:
        print(f'{n=} означает {r=}')

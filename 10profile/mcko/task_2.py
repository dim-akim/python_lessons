answers = []
for n in range(1, 100):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += '10'
    else:
        n2 = '1' + n2 + '00'
    r = int(n2, 2)
    if r > 107:
        answers.append(n)
        print(f'{n=} {n2=} {r=}')
print(min(answers))

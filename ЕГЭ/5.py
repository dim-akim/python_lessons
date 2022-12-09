for n in range(1, 100):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        r = '1' + bin_n + '0'
    else:
        r = '11' + bin_n + '11'
    # print(n, int(r, base=2))


s = '1' * 84

while '11111' in s:
    s = s.replace('222', '1', 1)
    s = s.replace('111', '2', 1)

# print(s)


count = 0
for a in 'ИВАН':
    for b in 'ИВАН':
        for c in 'ИВАН':
            for d in 'ИВАН':
                for e in 'ИВАН':
                    word = a+b+c+d+e
                    if 'И' in word:
                        count += 1

print(count)

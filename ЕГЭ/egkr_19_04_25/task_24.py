with open('24_21717.txt') as file:
    line = file.readline()

amount = 130
min_length = 10000
line = line.split('RSQ')
for i in range(len(line) - amount):
    s = 'RSQ'.join(line[i:i + amount + 1])
    if i + amount < len(line) - 1:
        s += 'R'
    length = len(s)
    if length < min_length:
        print(f'{length=} {s=}')
        min_length = length

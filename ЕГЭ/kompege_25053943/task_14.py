sum_lst = []

for x in '0123456789A':
    for y in '0123456789ABCD':
        number = int(f'{y}23{x}C', 14) + int(f'A{x}910', 11)
        if number % 23 == 0:
            sum_lst.append((int(x, 11) + int(y, 14), number // 23))

print(sorted(sum_lst))

alpha = '0123456789ABCDEFGHI'

for x in alpha:
    value = int(f'98897{x}21', 19) + int(f'2{x}923', 19)
    if value % 18 == 0:
        print(f'{x=} {value // 18}')

'9A87x21_12 + 2x68_14 - 1x2F4_16'

for x in '0123456789AB':
    val = int(f'9A87{x}21', 12) + int(f'2{x}68', 14) - int(f'1{x}2F4', 16)
    if val % 3 == 0:
        print(val // 3)

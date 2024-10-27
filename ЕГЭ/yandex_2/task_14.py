"""
14y5x2_14 + 31x2y3_14
"""

for x in '0123456789ABCD':
    for y in '0123456789ABCD':
        number = int(f'14{y}5{x}2', 14) + int(f'31{x}2{y}3', 14)
        if number % 9 == 0:
            print(f'{x=} {y=} {int(x, 14) + int(y, 14)} {number // 9=}')

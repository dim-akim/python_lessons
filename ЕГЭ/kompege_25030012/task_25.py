def even_4(n):
    div_list = []
    divisor = 2
    count = 0
    while divisor * divisor < n:
        if n % divisor == 0:
            div_list.append(divisor)
            divisor2 = n // divisor
            if divisor2 % 2 == 0:
                div_list.append(divisor2)
        divisor += 2
    if divisor * divisor == n and divisor % 2 == 0:
        div_list.append(divisor)
    return div_list


for number in range(69750, 100000000, 2):
    if str(number)[0] == '6' and '97' in str(number) and str(number)[-2] == '5':
        if len(even_4(number)) >= 4:
            print(f'{number=} {sum(even_4(number))}')

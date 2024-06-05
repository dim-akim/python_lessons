for number in range(123456, 987655):
    divisors = [1, number]
    for div in range(2, int(number ** 0.5) + 1):
        if number % div == 0:
            if div == number ** 0.5:
                divisors.append(div)
            else:
                divisors.append(div)
                divisors.append(number // div)
        if len(divisors) > 5:
            break
    divisors.sort()
    if len(divisors) == 5:
        print(f'{number=} {divisors}')

for number in range(200_000_000, 400_000_000 + 1):
    divisors = []
    for div in range(2, int(number ** 0.5) + 1):
        if number % div == 0:
            divisors.append(div)
            if number ** 0.5 != div:
                divisors.append(number // div)
        if len(divisors) > 2:
            break
    if len(divisors) == 2:
        print(f'{number=} {divisors}')

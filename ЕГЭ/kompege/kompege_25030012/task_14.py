for x in range(150):
    impres = 5 * 150**4 + 1 * 150**3 + x * 150**2 + 2 * 150 + 9
    impres += x * 150**3 + 2 * 150 + 3
    if impres % 149 == 0:
        print(f'{x=} {impres / 149 = }')

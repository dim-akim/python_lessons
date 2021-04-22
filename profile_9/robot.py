price = int(input())
before = 0
i_have_stocks = False

while price:  # while price != 0
    before = price
    price = int(input())

    if not i_have_stocks and price > before:
        price_min = price
        i_have_stocks = not i_have_stocks

    elif i_have_stocks and price < before:
        price_max = price
        i_have_stocks = not i_have_stocks
        break

print(price_max)
print(price_min)
print(price_max - price_min)

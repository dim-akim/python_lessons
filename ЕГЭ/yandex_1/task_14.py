number = 18 * 7**108 - 5 * 49**76 + 343**35 - 50
number = -number
number_49 = []

while number:
    number_49.append(number % 49)
    number //= 49

print(number_49[::-1])
print(sum(number_49))


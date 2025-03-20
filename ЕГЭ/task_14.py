# numbers = []
# for x in '1234567':
#     for y in range(8):
#         number = int(f'{x}01{y}4', 9) + int(f'{x}{y}544', 8)
#         if number % 89 == 0:
#             numbers.append(number // 89)
# print(sorted(numbers))


def to_base(number: int, base: int = 16) -> list:
    result = []
    while number:
        result.append(number % base)
        number //= base
    return result[::-1]
#
#
# number = 9**8 + 3**5 - 9
#
# print(to_base(number))

# 11353x12_25
def to_int(number: str, base: int):
    number = number[::-1]
    result = 0
    for i in range(len(number)):
        result += int(number[i]) * base**i
    return result

result = []
for x in range(25):
    number1 = 2 + 1 * 25 + x * 25**2 + 3 * 25**3 + 5 * 25**4 + 3 * 25**5 + 1 * 25**6 + 1 * 25**7
    number1 += 1 + 2 * 25 + x * 25**2 + 5 * 25**3 + 3 * 25**4 + 1 * 25**5

    number2 = to_int('11353012', 25) + 2 * x * 25**2 + to_int('135021', 25)

    if number2 % 24 == 0:
        result.append(number2 // 24)

print(max(result))

def to_base(n, base):
    answer = []
    while n > 0:
        answer.append(n % base)
        n //= base
    return answer[::-1]


number = 5 * 729**2024 + 3 * 243**1413 - 7 * 81**169 - 2 * 9**107 + 3017
n27 = to_base(number, 27)
answer = []
for digit in n27:
    if digit % 2 == 0 and digit <= 25:
        answer.append(digit)

print(sum(answer))

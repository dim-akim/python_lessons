with open('17_10719.txt') as file:
    numbers = [int(line) for line in file]

answer = []
for i in range(len(numbers) - 3):
    a, b = numbers[i], numbers[i + 3]
    if abs(a) % 100 == 13 and abs(b) % 100 != 13 or abs(b) % 100 == 13 and abs(a) % 100 != 13:
        answer.append(a + b)

print(f'{len(answer)=} {max(answer)=}')

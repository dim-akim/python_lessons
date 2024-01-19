with open('17_56545.txt') as file:
    numbers = [int(line) for line in file]

for i in range(len(numbers)):
    if numbers[i] == 7:
        print(f'{i=} {numbers[i]=}')

count = 0
with open('9') as file:
    for line in file:
        numbers = sorted(int(i) for i in line.split())
        cond1 = sum(1 for number in numbers if numbers.count(number) == 1) == 3
        cond2 = (len([number for number in numbers if number % 2 == 0]) >
                 len([number for number in numbers if number % 2 != 0]))
        cond3 = sum(numbers[4:]) > sum(numbers[:4]) * 2
        if cond1 + cond2 + cond3 >= 2:
            count += 1

print(count)

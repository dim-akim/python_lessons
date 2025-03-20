cars = []
parking = [-1] * 100

with open('26.txt') as file:
    n = int(file.readline())
    for line in file:
        time, duration, type = line.split()
        time = int(time)
        duration = int(duration)
        cars.append((time, time+duration, type))

cars.sort()
count_a = 0
loosers = 0
for start, end, type in cars:
    if type == 'A':
        for i in range(100):
            if parking[i] <= start:
                parking[i] = end
                count_a += 1
                break
        else:
            loosers += 1
    else:
        for i in range(80, 100):
            if parking[i] <= start:
                parking[i] = end
                break
        else:
            loosers += 1

print(cars)
print(parking)
print(f'{count_a=} {loosers=}')

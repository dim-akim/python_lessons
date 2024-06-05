with open('26_7602.txt') as file:
    k = int(file.readline().strip())
    n = int(file.readline().strip())
    passengers = []
    for line in file:
        passengers.append([int(i) for i in line.split()])

passengers.sort()

cells = [0] * k
last_cell = 0
total = 0
for start, end in passengers:
    for i in range(len(cells)):
        if cells[i] == 0 or cells[i] < start:
            cells[i] = end
            last_cell = i + 1
            total += 1
            break

print(total, last_cell)

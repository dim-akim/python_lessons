with open('24_11892.txt') as file:
    line = file.readline().strip()

lines = line.split('Y')

for line in lines:
    if line.count('X') >= 500:
        line_x = line.split('X')
        print(line_x)
        print(len(line_x[20]))
        print(len(line))

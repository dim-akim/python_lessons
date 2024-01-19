with open('24_11465.txt') as file:
    line = file.readline().strip()

line = line.replace('B', 'A').replace('C', 'A').replace('8', '9')
# line = line.replace('A9', 'XX').replace('9A', 'XX')

with open('24_result.txt', 'w') as file:
    file.write(line)

print(line)

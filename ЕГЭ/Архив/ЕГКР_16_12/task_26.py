with open('26_test.txt') as file:
    n, k = [int(i) for i in file.readline().split()]
    lines = [int(line) for line in file]

print(f'{n=} {k=}')
print(lines)

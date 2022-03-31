files = []

with open('26_test.txt') as file:
    S, n = [int(x) for x in file.readline().split()]
    for line in file:
        files.append(int(line))

files.sort()
max_sum = 0
i = 0

while max_sum <= S:
    if max_sum + files[i] < S:
        max_sum += files[i]
        i += 1
    else:
        break

max_files = i
max_number = files[max_files - 1]
print(f'{i=}   {max_sum=}   {max_number=}')

max_sum = max_sum - max_number

for i in range(max_files - 1, n):
    if max_sum + files[i] <= S:
        max_number = files[i]

print(files)
print(max_files, max_number)

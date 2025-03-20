with open('26_10726.txt') as file:
    films = []
    for line in file:
        start, end = line.split()
        films.append((int(start), int(end)))
films.sort()


total_length = 0
max_length = 0
last_start = last_end = 0
for start, end in films:
    if end <= last_end:
        continue
    if start <= last_end:
        total_length -= last_end - last_start
        last_end = end
    else:
        last_start, last_end = start, end

    cur_length = last_end - last_start
    max_length = max(max_length, cur_length)
    total_length += cur_length


print(films)
print(f'{total_length=} {max_length=}')

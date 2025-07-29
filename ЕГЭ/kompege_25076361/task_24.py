with open('24_19489.txt') as file:
    line = file.readline()


max_length = 0
lines = ['SFWW' + i + 'WSFW' for i in line.split('WSFWW')]

for line in lines:

    left = right = count_wwf = 0
    while right < len(line):
        while count_wwf < 121 and right <= len(line):
            if line[right:right+3] == 'WWF':
                count_wwf += 1
                right += 3
            else:
                right += 1
        s = line[left:right - 1]
        if len(s) > max_length:
            print(f'{count_wwf=} {len(s)=} {s=}')
            max_length = len(s)
        while count_wwf > 120:
            if line[left:left+3] == 'WWF':
                count_wwf -= 1
            left += 1

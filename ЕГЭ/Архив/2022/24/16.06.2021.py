minN = 1000000
with open('24_test.txt', 'r') as file:
    for line in file:
        count = line.count('N')
        if count < minN:
            slovar = {letter: 0 for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
            for letter in line:
                if letter == '\n':
                    continue
                slovar[letter] += 1
                minN = count

max_count = 0
for letter in slovar:
    if slovar[letter] >= max_count:
        max_count = slovar[letter]
        print(letter, max_count)

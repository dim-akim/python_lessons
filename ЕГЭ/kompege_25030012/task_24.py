with open('24_10724_redacted.txt') as file:
    line = file.readline()

alphabet = 'QWRTYUIOPSGHJKLZXVNM'

for letter in alphabet:
    line = line.replace(letter, '*')

line = sorted(line.split('*'), key=len, reverse=True)

for i in range(10):
    print(f'{line[i]=} {len(line[i])=}')

with open('24-33196.txt') as file:
    #     chastota = {letter: 0 for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    #     for line in file:
    #         for i in range(len(line) - 1):
    #             if line[i] == 'A':
    #                 symbol = line[i+1]
    #                 chastota[symbol] += 1
    #
    # maxS = 0
    # for letter in chastota:
    #     if chastota[letter] > maxS:
    #         maxS = chastota[letter]
    #         print(letter, maxS)

    letters = ''
    for line in file:
        for i in range(len(line) - 1):
            if line[i] == 'A':
                letters += line[i+1]

maxS = 0
for i in letters:
    count = letters.count(i)
    if count > maxS:
        maxS = count
        print(i, maxS)

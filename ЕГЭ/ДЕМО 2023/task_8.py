alphabet = '01234567'

count = 0
for a in alphabet[1:]:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                for e in alphabet:
                    number = a + b + c + d + e
                    if (number.count('6') == 1 and
                        '61' not in number and
                        '16' not in number and
                        '63' not in number and
                        '36' not in number and
                        '65' not in number and
                        '56' not in number and
                        '67' not in number and
                        '76' not in number):
                        count += 1

print(f'{count=}')
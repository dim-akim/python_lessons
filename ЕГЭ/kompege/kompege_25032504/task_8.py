count = 0
for a in '12345678':
    for b in '012345678':
        for c in '012345678':
            for d in '012345678':
                for e in '012345678':
                    number = a + b + c + d + e
                    if (number.count('3') == 1 and
                        '53' not in number and '35' not in number and
                        '63' not in number and '36' not in number and
                        '73' not in number and '37' not in number and
                        '83' not in number and '38' not in number):
                            count += 1
print(count)

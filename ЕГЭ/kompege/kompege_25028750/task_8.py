alphabet = '0123456789ABCDEFG'
count = 0
for a1 in '2468ACEG':
    for a2 in '04689ACEFG':
        for a3 in '04689ACEFG':
            for a4 in '04689ACEFG':
                for a5 in '04689ACEFG':
                    for a6 in '04689ACEFG':
                        number = a1 + a2 + a3 + a4 + a5 + a6
                        if (a1 != a2 and a1 != a3 and a1 != a4 and a1 != a5 and a1 != a6 and
                        a2 != a3 and a2 != a4 and a2 != a5 and a2 != a6 and
                        a3 != a4 and a2 != a5 and a2 != a6 and
                        a5 != a5 and a4 != a6 and a5 != a6):
                            count += 1
print(f'{count=}')

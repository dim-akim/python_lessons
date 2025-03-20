def b(n):
    answer = []
    if n == 1:
        for a in '13579':
            answer.append(a)
    elif n == 2:
        for a in '13579':
            for b in '13579':
                answer.append(a + b)
    elif n == 3:
        for a in '13579':
            for b in '13579':
                for c in '13579':
                    answer.append(a + b + c)
    elif n == 4:

        for a in '13579':
            for b in '13579':
                for c in '13579':
                    for d in '13579':
                        answer.append(a + b + c + d)
    return answer


mask = '1A2157B4'

for A in range(0, 10, 2):
    if int(f'1{A}21574') % 133 == 0:
        print(int(f'1{A}21574'), int(f'1{A}21574') // 133)
    for i in range(1, 4):
        for B in b(i):
            if int(f'1{A}2157{B}4') % 133 == 0:
                print(int(f'1{A}2157{B}4'), int(f'1{A}2157{B}4') // 133)

count = 0
for a in 'ГПРБЛ':
    for b in 'ГИПЕРБОЛА':
        for c in 'ГИПЕРБОЛА':
            for d in 'ГИПЕРБОЛА':
                for e in 'ГИПЕРБОЛА':
                    for f in 'ГПРБЛ':
                        word = a + b + c + d + e + f
                        flag = True
                        for i in range(1, len(word) - 1):
                            if word[i] in 'ИЕОА' and word[i-1] in 'ГПРБЛ' and word[i+1] in 'ГПРБЛ':
                                flag = False
                                break
                        if flag:
                            print(word)
                            count += 1
print(count)

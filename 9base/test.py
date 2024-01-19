k = 1
for a in 'ГД':
    for b in 'ГОД':
        for c in 'ГОД':
            for d in 'ГОД':
                for e in 'ГОД':
                    for f in 'ГОД':
                        word = a + b + c + d + e + f
                        print(f"{k}. {word}")
                        k += 1

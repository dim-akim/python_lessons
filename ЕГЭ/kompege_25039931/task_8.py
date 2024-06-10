"""
ПРОСТО - 6!/2! - 5*24

ОО____ - 24
_ОО___ - 24
__ОО__ - 24
___ОО_ - 24
____ОО - 24

"""
total = 0
for a in 'ПРОСТО':
    for b in 'ПРОСТО':
        for c in 'ПРОСТО':
            for d in 'ПРОСТО':
                for e in 'ПРОСТО':
                    for f in 'ПРОСТО':
                        word = a + b + c + d + e + f
                        if (word.count('П') == 1 and
                                word.count('Р') == 1 and
                                word.count('О') == 2 and
                                word.count('С') == 1 and
                                word.count('Т') == 1 and
                                'ОО' not in word):
                            if word == 'ПРОСТО':
                                print(word)
                            total += 1
print(total / 4)

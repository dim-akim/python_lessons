import itertools


alpha = 'ПАРИЖАНКА'
answer = set()
for letters in itertools.permutations(alpha):
    word = ''.join(letters)
    if (word.count('АИ') + word.count('АА') + word.count('ИА') == 1) and (
            'ААА' not in word and
            'ИАА' not in word and
            'АИА' not in word and
            'ААИ' not in word
    ):
        answer.add(word)

print(sorted(answer))
print(len(answer))

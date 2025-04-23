def is_ok(number):
    pass


answer = []
alphabet = '0123456789ABC'
for n1 in alphabet[1:]:
    for n2 in alphabet:
        for n3 in alphabet:
            for n4 in alphabet:
                for n5 in alphabet:
                    number = n1 + n2 + n3 + n4 + n5
                    if all(
                        [number.count(x) == 1 for x in number] +
                        [int(number[i], 13) % 2 != int(number[i+1], 13) % 2 for i in range(len(number) - 1)]
                    ):
                        answer.append(number)

print(answer)
print(len(answer))

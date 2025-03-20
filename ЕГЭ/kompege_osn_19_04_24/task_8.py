alphabet = '0123456789ABCDE'

result = []
for n1 in alphabet[1:]:
    for n2 in alphabet:
        for n3 in alphabet:
            for n4 in alphabet:
                for n5 in alphabet:
                    number = n1 + n2 + n3 + n4 + n5
                    alpha_amount = 0
                    for s in number:
                        if s.isalpha():
                            alpha_amount += 1
                    if number.count('8') == 1 and alpha_amount >= 2:
                        result.append(number)

# print(result)
# print(len(result))


counter = 0
dct = "0123456789abcde"
arr = []
for n1 in "123456789abcde":
    for n2 in dct:
        for n3 in dct:
            for n4 in dct:
                for n5 in dct:
                    cntr = 0
                    for i in [n1, n2, n3, n4, n5]:
                        if int(i, 15) > 9:
                            cntr += 1
                    number = n1 + n2 + n3 + n4 + n5
                    if number.count("8") == 1 and cntr >= 2:
                        counter += 1
                        arr.append(number)

# print(arr)
# print(len(arr))

for i in range(len(result)):
    a, b = result[i].lower(), arr[i]
    if a != b:
        print(a, b)

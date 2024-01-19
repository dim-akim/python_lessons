# total = 0
#
# for a in '0123':
#     for b in 'ЕГЭ':
#         for c in 'ЕГЭ':
#             for d in 'ЕГЭ':
#                 for e in 'ЕГЭ':
#                     word = a + b + c + d + e
#                     if word.count('Г') == 1:
#                         total += 1
#
# print(total)

total = 0

for a in range(1, 4):
    for b in range(4):
        for c in range(4):
            if a + c > b:
                total += 1

print(total)

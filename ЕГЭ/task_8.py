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

# total = 0
#
# for a in range(1, 4):
#     for b in range(4):
#         for c in range(4):
#             if a + c > b:
#                 total += 1
#
# print(total)

# count = 1
# for a in 'АОУ':
#     for b in 'АОУ':
#         for c in 'АОУ':
#             for d in 'АОУ':
#                 for e in 'АОУ':
#                     word = a + b + c + d + e
#                     count += 1
#                     if count == 210:
#                         print(word)

# total = 0
# for a in 'СЛН':
#     for b in 'ОУА':
#         for c in 'СЛН':
#             for d in 'ОУА':
#                 for e in 'СЛН':
#                     word = a + b + c + d + e
#                     if word.count('С') == 1:
#                         total += 1
# print(total)
#
# total = 0
#
# for a in 'АБВГ':
#     for b in 'АБВГ':
#         for c in 'АБВГ':
#             for d in 'АБВГ':
#                 for e in 'АБВГ':
#                     word = a + b + c + d + e
#                     if word.count('А') == 1:
#                         total += 1
#
# print(total)

def f(n):
    s = str(n)
    if len(s) == 11:
        return 1
    podr = []
    for i in range(9):
        if (int(s[-1]) + i) % 2 == 0 and i > int(s[-1]):
            podr.append(int(s+str(i)))
        if (int(s[-1]) + i) % 2 != 0 and i < int(s[-1]):
            podr.append(int(s + str(i)))
            
    return sum(f(i) for i in podr)


print(sum(f(i) for i in range(1, 9)))

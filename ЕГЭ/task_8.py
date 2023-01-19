# count = 0
# a = 'Е'
# for b in 'ЕГЭИНФ':
#     for c in 'ЕГЭИНФ':
#         for d in 'ЕГЭИНФ':
#             for e in 'ЕГЭИНФ':
#                 for f in 'ЭИ':
#                     s = a + b + c + d + e + f
#                     if s.count('ФИ') == 2 and s.count('ЕГЭ') == 0:
#                         count += 1
# print(count)

start = int('10000', base=8)
stop = int('77777', base=8)
count = 0

for number in range(start, stop+1):
    number = oct(number)[2:]
    if len(number) == len(set(number)):
        flag = False
        for i in range(len(number)-1):
            if int(number[i]) % 2 == int(number[i+1]) % 2:
                flag = True
                break
        if not flag:
            count += 1

print(count)

count = 0
for a in '246':
    for b in '357':
        for c in '0246':
            if c == a:
                continue
            for d in '357':
                # if d == b:
                #     continue
                for e in '0246':
                    # if e == a or e == c:
                    #     continue
                    print(f'{a=}{b=}{c=}{d=}{e=}')
#                     if a != c and a != e and c != e and b != d:
#                         number = a + b + c + d + e
#                         # for i in number:
#                         #     if number.count(i) > 1:
#                         #         continue
#                         count += 1
# for a in '357':
#     for b in '0246':
#         for c in '357':
#             if c == a:
#                 continue
#             for d in '0246':
#                 if d == b:
#                     continue
#                 for e in '357':
#                     if e == a or e == c:
#                         continue
#                     if a != c and a != e and c != e and b != d:
#                         number = a + b + c + d + e
#                         # for i in number:
#                         #     if number.count(i) > 1:
#                         #         continue
#                         count += 1
# print(count)

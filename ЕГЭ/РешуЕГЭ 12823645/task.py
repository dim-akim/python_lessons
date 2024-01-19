# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x and not y) == (z or not w)) <= (x and z)) is False:
#                     print(x, y, z, w)
#
# for i in range(1, 100):
#     n = bin(i)[2:]
#     if n[-1] == '0':
#         n += '00'
#     else:
#         n += '11'
#     r = int(n, 2)
#     print(f'{i=} {n=} {r=}')
# import turtle
#
#
# t = turtle.Turtle()
# t.lt(90)
# turtle.tracer(10)
# step = 50
#
# for i in range(5):
#     t.fd(7 * step)
#     t.rt(90)
#     t.fd(4 * step)
#     t.rt(90)
#
# t.up()
# for _x in range(10):
#     for _y in range(10):
#         x, y = _x * step, _y * step
#         t.goto(x, y)
#         t.dot(4)
#
# turtle.mainloop()
# count = 0
# for a in 'ABCDEF':
#     for b in 'ABCDEF':
#         for c in 'ABCDEF':
#             for d in 'ABCDEF':
#                 for e in 'ABCDEF':
#                     word = a + b + c + d + e
#                     if word[0] != 'F' and word[-1] != 'A':
#                         count += 1
# print(count)
# s = '>' + '1' * 26 + '2' * 10 + '3' * 14
#
# while '>1' in s or '>2' in s or '>3' in s:
#     if '>1' in s:
#         s = s.replace('>1', '22>', 1)
#     if '>2' in s:
#         s = s.replace('>2', '2>', 1)
#     if '>3' in s:
#         s = s.replace('>3', '1>', 1)
# print(s)
# print(sum(int(i) for i in s[:-1]))
# min_80 = 10000000000000000
# for x in '123456789AB':
#     for y in '123456789AB':
#         s = int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)
#         if s % 80 == 0:
#             min_80 = min(s, min_80)
#
# print(f'{x=} {y=} {min_80/80=}')
# for A in range(1, 1000):
#     flag = True
#     for x in range(1, 10000):
#         if ((120 % A == 0) and ((x % A != 0) <= ((x % 18 == 0) <= (x % 24 != 0)))) is False:
#             flag = False
#     if flag:
#         print(A)

#
# def f(n):
#     if n <= 2:
#         return n
#     return f(n-1) * f(n-2)
#
# print(f(7))
# with open('17.txt') as file:
#     numbers = [int(line) for line in file]
# max_division = count = 0
# for i in range(len(numbers)-1):
#     for j in range(i+1, len(numbers)):
#         a, b = numbers[i], numbers[j]
#         division = a - b
#         if division % 60 == 0:
#             if a % 15 == 0 or b % 15 == 0:
#                 count += 1
#                 max_division = max(max_division, division)
# print(count, max_division)

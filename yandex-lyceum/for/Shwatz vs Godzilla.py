"""
Арнольд Шварценеггер стреляет в ужасного монстра Годзиллу из дробовика.
Нужно найти общую величину урона, нанесённого Годзилле выстрелом.

Подсказка: возможно, для быстрой работы программы вам пригодится алгоритм Евклида.

Формат ввода
Сначала вводится количество дробинок.
Затем урон от каждой дробинки. Урон от каждой дробинки выражается простой дробью,
её числитель и знаменатель вводятся на отдельных строках.

Формат вывода
Суммарный урон, выраженный простой несократимой дробью с дробной чертой между числителем и знаменателем.

Пример
Ввод	Вывод
3       3/50
1
60
1
30
1
100
"""

n = int(input())
chisl = int(input())
znam = int(input())

for i in range(1, n):
    chisl_new = int(input())
    znam_new = int(input())
    if znam == znam_new:
        chisl += chisl_new
    else:
        chisl *= znam_new
        chisl_new *= znam
        chisl += chisl_new
        znam *= znam_new

if znam % chisl == 0:
    nod1 = chisl
else:
    nod1 = chisl
    nod2 = znam
    while nod1 != nod2:
        if nod1 > nod2:
            nod1, nod2 = nod2, nod1
        nod2, nod1 = nod2 - nod1, nod1

print(chisl // nod1, znam // nod1, sep="/")

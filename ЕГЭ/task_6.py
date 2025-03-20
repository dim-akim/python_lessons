from turtle import *


tracer(10)
size = 50
lt(90)

for i in range(3):
    fd(size * 2)
    rt(90)
    fd(size * 3)
    lt(90)
rt(180)
fd(size * 6)
rt(90)
fd(size * 9)
up()
bk(size * 3)
rt(90)
down()
for i in range(2):
    fd(size * 1)
    rt(90)
    fd(size * 2)
    lt(90)
rt(180)
fd(size * 3)
rt(90)
fd(size * 4)
rt(90)
fd(size * 1)

up()
for x in range(-5 * size, 10 * size, size):
    for y in range(-5 * size, 10 * size, size):
        goto(x, y)
        dot(3)

done()

from turtle import *


tracer(0)
line = 50
lt(90)

for i in range(4):
    lt(45)
    fd(line * 5)
    lt(45)
    fd(line * 6)

up()

for x in range(-15 * line, 5 * line, line):
    for y in range(-15 * line, 5 * line, line):
        goto(x, y)
        dot(3)

update()
done()

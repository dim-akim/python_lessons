from turtle import *


tracer(0)
line = 20

for i in range(7):
    right(45)
    forward(11 * line)
    right(45)

penup()
for x in range(-10 * line, 10 * line, line):
    for y in range(-10 * line, 10 * line, line):
        goto(x, y)
        dot(3)
tracer(1)

done()

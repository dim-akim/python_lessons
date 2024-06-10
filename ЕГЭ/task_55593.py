from turtle import *

tracer(10)
size = 10
x = 10
for i in range(6):
    fd(x * size)
    right(90)
    fd(x * size)
    left(90)
    fd(x * size)
    right(90)

penup()

for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * size, y * size)
        dot(3)



done()

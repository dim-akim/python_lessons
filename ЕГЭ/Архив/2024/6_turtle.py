from turtle import *


t = Turtle()
t.speed(0)
t.left(90)

size = 10
for i in range(2):
    t.fd(10*size)
    t.rt(90)
    t.fd(20 * size)
    t.rt(90)
t.up()
t.fd(3*size)
t.rt(90)
t.fd(7*size)
t.lt(90)
t.down()
for i in range(2):
    t.fd(70*size)
    t.rt(90)
    t.fd(90 * size)
    t.rt(90)

t.up()
for _x in range(21):
    for _y in range(11):
        x = _x * size
        y = _y * size
        t.goto(x, y)
        t.dot(4)

mainloop()

from turtle import *


t = Turtle()
t.speed(0)
t.left(90)

size = 40
for i in range(10):
    t.forward(5 * size)
    t.right(60)

t.up()
for x in range(20):
    for y in range(-5, 20):
        t.goto(x * size, y * size)
        t.dot(5)
exitonclick()

from turtle import *


def create_ball(x, y):
    t = Turtle()
    t.speed(0)
    t.shape('circle')
    t.up()
    t.goto(x, y)

    return t


def move(something):
    pos = something.position()
    x = pos[0]
    y = pos[1]

    something.goto(x + 1, y)
    print(pos)


ball = create_ball(-100, 100)
while True:  # Бесконечный цикл
    move(ball)

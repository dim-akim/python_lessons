from turtle import *


def create_ball(x, y):
    t = Turtle()
    t.speed(0)
    t.shape('circle')
    t.up()
    t.goto(x, y)

    return t


def move(something):
    global speed_x
    pos = something.position()
    x = pos[0]
    y = pos[1]

    if x >= 465 or x <= -465:
        speed_x = -speed_x

    something.goto(x + speed_x, y)
    print(pos)


ball = create_ball(-100, 100)
speed_x = 1
while True:  # Бесконечный цикл
    move(ball)

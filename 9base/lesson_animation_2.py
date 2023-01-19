from turtle import *


def create_ball(x, y):
    t = Turtle()
    t.speed(0)
    t.shape('circle')
    t.up()
    t.goto(x, y)

    return t


def move(something):
    print('Я подвинуль')


ball = create_ball(-400, 395)
while True:  # Бесконечный цикл
    move(ball)

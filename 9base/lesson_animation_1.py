from turtle import *


def create_ball(x, y):
    t = Turtle()
    t.shape('circle')
    t.speed(0)
    t.up()
    t.goto(x, y)

    return t


def move(something):
    print('Я подвинуль')


ball = create_ball(-100, 100)

while True:  # Бесконечный цикл
    move(ball)

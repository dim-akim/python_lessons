from turtle import *


def draw_house(x, y, width, height):
    wall_height = height * 2 / 3
    draw_wall(x, y, width, wall_height)

    roof_y = y + wall_height
    roof_height = height - wall_height
    draw_roof(x, roof_y, width, roof_height)

    window_width = width / 3
    window_height = wall_height / 3
    window_x = x + window_width
    window_y = y + window_height
    draw_window(
        window_x,
        window_y,
        window_width,
        window_height
    )


def draw_wall(x, y, width, height):
    wall = Turtle()
    wall.up()
    wall.goto(x, y)
    wall.down()

    for i in range(2):
        wall.forward(width)
        wall.left(90)
        wall.forward(height)
        wall.left(90)
    print('Я прораб - сделяль стена')


def draw_roof(x, y, width, height):
    roof = Turtle()
    roof.up()
    roof.goto(x, y)
    roof.down()

    roof.goto(x + width / 2, y + height)
    roof.goto(x + width, y)
    roof.goto(x, y)
    print('Я прораб - сделяль крыша')


def draw_window(x, y, width, height):
    window = Turtle()
    window.up()
    window.goto(x, y)
    window.down()

    for i in range(2):
        window.forward(width)
        window.left(90)
        window.forward(height)
        window.left(90)

    window.goto(x, y + height * 2 / 3)
    window.goto(x + width, y + height * 2 / 3)
    window.up()
    window.goto(x + width / 2, y + height * 2 / 3)
    window.down()
    window.goto(x + width / 2, y)
    print('Я прораб - сделяль акошка')


draw_house(-100, -100, 300, 300)

import turtle

screen = turtle.Screen()
screen.setup(0.75, 0.75)

house = turtle.Turtle()
house.pensize(4)
house.speed(0)
house.shape('turtle')


def draw_house(x, y, line):  # define - определить
    # Перемещение
    house.up()
    house.goto(x, y)
    house.down()

    # СТЕНЫ
    # wall_color = screen.textinput('Цвет стены', 'Напишите цвет на английском языке')
    wall_color = 'blue'

    house.color('black', wall_color)
    house.begin_fill()
    house.forward(line)
    house.right(90)
    house.forward(line)
    house.right(90)
    house.forward(line)
    house.right(90)
    house.forward(line)
    house.end_fill()

    # КРЫША
    # roof_color = screen.textinput('Цвет крыши', 'Напишите цвет на английском языке')
    roof_color = 'brown'

    house.color('black', roof_color)
    house.begin_fill()
    house.right(30)
    house.forward(line)
    house.right(120)
    house.forward(line)
    house.right(30)
    house.end_fill()
    # ОКНО
    house.up()
    house.forward(line / 3)
    house.right(90)
    house.forward(line / 3)
    house.down()

    # window_color = screen.textinput('Цвет окна', 'Напишите цвет на английском языке')
    window_color = 'yellow'

    house.color('black', window_color)
    house.begin_fill()
    house.forward(line / 3)
    house.left(90)
    house.forward(line / 3)
    house.left(90)
    house.forward(line / 3)
    house.left(90)
    house.forward(line / 3)
    house.end_fill()
    # ЧЕРДАК
    house.up()
    house.forward(line / 3)
    house.left(90)
    house.forward(line / 6)
    house.right(90)
    house.forward(line / 6)
    house.right(90)
    house.down()

    # attic_color = screen.textinput('Цвет чердака', 'Напишите цвет на английском языке')
    attic_color = 'orange'

    house.color('black', attic_color)
    house.begin_fill()
    house.circle(line / 10)
    house.end_fill()

draw_house(300, 100, 200)
draw_house(100, 50, 100)
draw_house(-100, 50, 50)


def draw_circle(x, y, radius, color):
    house.up()
    house.goto(x, y)
    house.down()

    house.color(color)
    house.begin_fill()
    house.circle(radius)
    house.end_fill()


def draw_cloud(x, y, radius, is_raining):
    # 1 ряд
    draw_circle(x, y, radius, 'lightgrey')
    draw_circle(x + radius * 1.5, y, radius, 'lightgrey')
    draw_circle(x + radius * 2.5, y, radius, 'lightgrey')
    draw_circle(x + radius * 4, y, radius, 'lightgrey')

    # Дождик
    if is_raining == 1:
        house.up()
        house.goto(x, y - radius * 0.5)
        house.down()
        house.goto(x - radius * 0.5, y - radius * 1.5)

        house.up()
        house.goto(x + radius, y - radius * 0.5)
        house.down()
        house.goto(x + radius * 0.5, y - radius * 1.5)

        house.up()
        house.goto(x + radius * 2, y - radius * 0.5)
        house.down()
        house.goto(x + radius * 1.5, y - radius * 1.5)

    # 2 ряд
    draw_circle(x + radius * 0.5, y + radius, radius, 'lightgrey')
    draw_circle(x + radius * 2, y + radius, radius, 'lightgrey')
    # 3 ряд
    draw_circle(x + radius, y + radius * 2, radius, 'lightgrey')

draw_cloud(200, 200, 50, 1)
draw_cloud(0, 200, 30, 0)

turtle.done()

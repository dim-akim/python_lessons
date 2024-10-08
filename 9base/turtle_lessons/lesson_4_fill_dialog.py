import turtle

screen = turtle.Screen()
screen.setup(0.5, 0.5)

house = turtle.Turtle()
house.pensize(4)
house.speed(3)
house.shape('turtle')

line = 200

# СТЕНЫ
wall_color = screen.textinput('Цвет стены', 'Напишите цвет на английском языке')

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
house.right(30)
house.forward(line)
house.right(120)
house.forward(line)
house.right(30)
# ОКНО
house.up()
house.forward(line / 3)
house.right(90)
house.forward(line / 3)
house.down()

house.forward(line / 3)
house.left(90)
house.forward(line / 3)
house.left(90)
house.forward(line / 3)
house.left(90)
house.forward(line / 3)

# ЧЕРДАК
house.up()
house.forward(line / 3)
house.left(90)
house.forward(line / 6)
house.right(90)
house.forward(line / 6)
house.right(90)
house.down()

house.circle(line / 10)

turtle.done()

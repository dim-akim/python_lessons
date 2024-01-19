import turtle

bob = turtle.Turtle()
line = turtle.numinput("Размер линии", "Введите размер линии: от 17 до 170")
radius = turtle.numinput("Размер радиуса", "Введите размер рдиуса: от 17 до 170")
text = turtle.textinput("цвет фигуры", "Введите цвет на руссссском")
# квадрат
if text == "розовый":
    wall_color = ("pink")
elif text == "голубой":
    wall_color = ("blue")
elif text == "фиолетовый":
    wall_color = ("violet")
elif text == "жёлтый":
    wall_color = ("yellow")

bob.color("black", wall_color)
bob.begin_fill()
bob.forward(line)
bob.right(90)
bob.forward(line)
bob.right(90)
bob.forward(line)
bob.right(90)
bob.forward(line)
bob.end_fill()
# 1круг

bob.color("black", wall_color)
bob.right(90)
bob.forward(line / 2)
bob.begin_fill()
text = turtle.textinput("цвет фигуры", "Введите цвет на руссссском")
if text == "розовый":
    wall_color = ("pink")
elif text == "голубой":
    wall_color = ("blue")
elif text == "фиолетовый":
    wall_color = ("violet")
elif text == "жёлтый":
    wall_color = ("yellow")
bob.circle(radius)
bob.end_fill()
# 2круг

bob.color("black", wall_color)
bob.forward(line / 2)
bob.right(90)
bob.forward(line / 2)
bob.begin_fill()
text = turtle.textinput("цвет фигуры", "Введите цвет на руссссском")
if text == "розовый":
    wall_color = ("pink")
elif text == "голубой":
    wall_color = ("blue")
elif text == "фиолетовый":
    wall_color = ("violet")
elif text == "жёлтый":
    wall_color = ("yellow")
bob.circle(radius)
bob.end_fill()
# 3круг

bob.color("black", wall_color)
bob.forward(line / 2)
bob.right(90)
bob.forward(line / 2)
bob.begin_fill()
text = turtle.textinput("цвет фигуры", "Введите цвет на руссссском")
if text == "розовый":
    wall_color = ("pink")
elif text == "голубой":
    wall_color = ("blue")
elif text == "фиолетовый":
    wall_color = ("violet")
elif text == "жёлтый":
    wall_color = ("yellow")
bob.circle(radius)
bob.end_fill()
# 4круг

bob.color("black", wall_color)
bob.forward(line / 2)
bob.right(90)
bob.forward(line / 2)
bob.begin_fill()
text = turtle.textinput("цвет фигуры", "Введите цвет на руссссском")
if text == "розовый":
    wall_color = ("pink")
elif text == "голубой":
    wall_color = ("blue")
elif text == "фиолетовый":
    wall_color = ("violet")
elif text == "жёлтый":
    wall_color = ("yellow")
bob.circle(radius)
bob.end_fill()

turtle.exitonclick()

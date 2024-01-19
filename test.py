import turtle

t = turtle.Turtle()

#квадрат

t.forward (100)
t.right(90)
t.forward (100)
t.right(90)
t.forward (100)
t.right(90)
t.forward (100)

#треугольник

t.up()
t.forward (50)
t.right(90)
t.down()
t.forward (100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

#прямоугольник

t.right(60)
t.up()
t.forward (50)
t.down()
t.forward (100)
t.right(90)
t.forward (50)
t.right(90)
t.forward (100)
t.right(90)
t.forward (50)

#параллелограм

t.up()
t.forward (50)
t.right(90)
t.forward(50)
t.down()
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)
t.left(60)
t.forward(50)
t.right(240)
t.forward(50)
turtle.exitonclick()
import turtle


joe = turtle.Turtle()
joe.pensize(4)
joe.speed(0)
line = 200
radius = 100

# 1 сторона
joe.forward(line / 2)
joe.color('cyan')
joe.begin_fill()
joe.circle(radius)
joe.end_fill()
joe.color('black')
joe.forward(line / 2)
joe.right(90)

# 2 сторона
joe.forward(line / 2)
joe.color('magenta')
joe.begin_fill()
joe.circle(radius)
joe.end_fill()
joe.color('black')
joe.forward(line / 2)
joe.right(90)

# 3 сторона
joe.forward(line / 2)
joe.color('yellow')
joe.begin_fill()
joe.circle(radius)
joe.end_fill()
joe.color('black')
joe.forward(line / 2)
joe.right(90)

# 4 сторона
joe.forward(line / 2)
joe.color('grey')
joe.begin_fill()
joe.circle(radius)
joe.end_fill()
joe.color('black')
joe.forward(line / 2)
joe.right(90)

joe.fd(line)
joe.right(90)
joe.fd(line)
joe.right(90)
joe.fd(line)
joe.right(90)
joe.fd(line)
joe.right(90)

turtle.exitonclick()

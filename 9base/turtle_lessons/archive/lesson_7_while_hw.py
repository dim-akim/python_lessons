import turtle


joe = turtle.Turtle()
joe.left(90)
joe.color('black', 'green')

line = 200
width = 40
n = 15

i = 0
while i < n:
    joe.begin_fill()
    joe.forward(line)
    joe.right(30)
    joe.forward(width)
    joe.right(120)
    joe.forward(width)
    joe.right(30)
    joe.forward(line)
    joe.right(180)
    joe.end_fill()
    i = i + 1

turtle.exitonclick()

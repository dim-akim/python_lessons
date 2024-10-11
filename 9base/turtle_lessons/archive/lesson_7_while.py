import turtle


joe = turtle.Turtle()

line = 100
n = 5

i = 0
while i < n:
    joe.forward(line)
    joe.right(360 / n)
    i = i + 1

turtle.exitonclick()

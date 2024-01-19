import turtle


joe = turtle.Turtle()
joe.left(90)
turtle.tracer(10)

line = 40
joe.width(4)
for i in range(2):
    joe.fd(5 * line)
    joe.left(90)
    joe.back(13 * line)
    joe.left(90)

joe.up()
joe.back(10 * line)
joe.right(90)
joe.fd(9 * line)
joe.left(90)
joe.down()

for i in range(2):
    joe.fd(11 * line)
    joe.left(90)
    joe.fd(7 * line)
    joe.left(90)

joe.up()

# for x in range(-10, 15):
#     for y in range(-10, 15):
#         joe.goto(x * line, y * line)
#         joe.dot(4)
joe.width(1)
for x in range(-10, 15):
    joe.goto(x * line, -10 * line)
    joe.down()
    joe.goto(x * line, 15 * line)
    joe.up()

for y in range(-10, 15):
    joe.goto(-10 * line, y * line)
    joe.down()
    joe.goto(15 * line, y * line)
    joe.up()

turtle.exitonclick()

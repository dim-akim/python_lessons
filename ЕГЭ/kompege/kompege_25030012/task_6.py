import turtle


t = turtle.Turtle()
t.left(90)
turtle.tracer(10)

scale = 20

# Алгоритм
t.right(90)
for i in range(3):
    t.right(45)
    t.fd(10 * scale)
    t.right(45)
t.right(315)
t.fd(10 * scale)
for i in range(2):
    t.right(90)
    t.fd(10 * scale)

t.up()
for x in range(-15 * scale, 15 * scale, scale):
    for y in range(-15 * scale, 15 * scale, scale):
        t.goto(x, y)
        t.dot(5)

print(29 * 7)

turtle.exitonclick()

import turtle


t = turtle.Turtle()
turtle.tracer(20)

step = 20
for i in range(10):
    t.goto(0*step, 2*step)
    t.goto(2*step, 0*step)
    t.goto(0*step, 10*step)
    t.goto(-2*step, 0*step)
    t.goto(0*step, 2*step)
    t.goto(6*step, 0*step)
    t.goto(0*step, -2*step)
    t.goto(-2*step, 0*step)
    t.goto(0*step, -10*step)
    t.goto(2*step, 0*step)
    t.goto(0*step, -2*step)
    t.goto(-6*step, 0*step)

t.penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        t.goto(x*step, y*step)
        t.dot(4)

turtle.exitonclick()

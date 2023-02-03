from turtle import *


tracer(10)
t = Turtle()
t.speed(0)
line = 30
t.lt(90)
t.color('black', 'green')
t.begin_fill()
for i in range(12):
    t.rt(60)
    t.fd(2 * line)
    t.rt(60)
    t.fd(2 * line)
    t.rt(270)
t.end_fill()
t.up()
t.color('blue')
t.pensize(4)


canvas = getcanvas()
count = 0
for x in range(10, -10, -1):
    for y in range(2, -18, -1):
        x_1 = x * line
        y_1 = y * line
        s = canvas.find_overlapping(x_1, -y_1, x_1, -y_1)
        print(f'{x_1=}, {y_1=}, {s=}')
        if (5,) == s:
            count += 1
            t.color('red')
        elif 4 in s:
            t.color('brown')
        else:
            t.color('blue')
        t.goto(x_1, y_1)
        t.dot(5)

print(count)

mainloop()

from turtle import *


def create_ball(x, y):
    t = Turtle()
    t.color('green')
    t.speed(2)
    t.shape('circle')
    t.up()
    t.goto(x, y)

    return t

def move(something):
    global speed_x
    global speed_y
    pos = something.position()
    x = pos[0]
    y = pos[1]

    if x >= 465 or x <= -465:
        speed_x = -speed_x
    if y >= 395 or y <= -395:
        speed_y = -speed_y

    something.goto(x + speed_x, speed_y + y)
    print(pos)

def create_player(x, y):
    t = Turtle()
    t.color('purple')
    t.speed(0)
    t.shape('square')
    t.shapesize(5, 1)
    t.up()
    t.goto(x, y)

    return t

def move_up_1():
    global player_1
    pos = player_1.position()
    x = pos[0]
    y = pos[1]

    player_1.goto(x, y + 10)
    print(pos)

def move_down_1():
    global player_1
    pos = player_1.position()
    x = pos[0]
    y = pos[1]

    player_1.goto(x , y - 10)
    print(pos)

def move_up_2():
    global player_2
    pos = player_2.position()
    x = pos[0]
    y = pos[1]

    player_2.goto(x, y + 10)
    print(pos)

def move_down_2():
    global player_2
    pos = player_2.position()
    x = pos[0]
    y = pos[1]

    player_2.goto(x , y - 10)
    print(pos)

window = Screen()
window.listen()#окно слушай событие
window.onkeypress(move_up_1, 'w')
window.onkeypress(move_up_2, 'Up')
window.onkeypress(move_down_1, 's')
window.onkeypress(move_down_2, 'Down')

player_1 = create_player(-200, 0)
player_2 = create_player(200, 0)


ball = create_ball(-100, 100)
speed_x = 3
speed_y = 3

while True:
    move(ball)
from turtle import *


def create_ball(x, y):
    t = Turtle()
    t.speed(0)
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

    something.goto(x + speed_x, y + speed_y)


def create_player(x, y):
    t = Turtle()
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


def move_down_1():
    global player_1
    pos = player_1.position()
    x = pos[0]
    y = pos[1]

    player_1.goto(x, y - 10)


def move_up_2():
    global player_2
    pos = player_2.position()
    x = pos[0]
    y = pos[1]

    player_2.goto(x, y + 10)


def move_down_2():
    global player_2
    pos = player_2.position()
    x = pos[0]
    y = pos[1]

    player_2.goto(x, y - 10)


def check_collisions_1(ball, player):
    global speed_x
    pos = player.position()  # Получаем позицию игрока
    x_player = pos[0]
    y_player = pos[1]
    pos = ball.position()  # Получаем позицию мячика
    x_ball = pos[0]
    y_ball = pos[1]

    if x_player-10 <= x_ball <= x_player+10 and y_player-50 <= y_ball <= y_player+50:
        speed_x = -speed_x


window = Screen()
window.listen()  # Окно, слушай события!
window.onkeypress(move_up_1, 'w')
window.onkeypress(move_down_1, 's')
window.onkeypress(move_up_2, 'Up')
window.onkeypress(move_down_2, 'Down')

player_1 = create_player(-400, 0)
player_2 = create_player(400, 0)

ball = create_ball(-100, 100)
speed_x = 4
speed_y = 4

while True:  # Бесконечный цикл
    move(ball)
    check_collisions_1(ball, player_1)

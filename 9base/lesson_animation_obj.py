from turtle import Turtle, TurtleScreen
import math
import random


class Base(Turtle):
    def __init__(self, color='white'):
        super().__init__()
        self.color(color)
        self.speed(0)
        self.up()


class Ball(Base):
    def __init__(self):
        super().__init__()
        self.shape('ball')
        self.speed_x = 0
        self.speed_y = 0


class Player(Base):
    players_count = 0

    def __init__(self, x=0, y=0, name=None):
        super().__init__()
        Player.players_count += 1
        self.shape('square')
        self.shapesize(5, 1)
        self.speed_y = 10
        self.dy = 0
        self.name = name if name else f'Player {Player.players_count}'
        self.goto(x, y)

    def move(self):
        self.sety(self.ycor() + self.dy)

    def move_up(self):
        self.dy = self.speed_y

    def move_down(self):
        self.dy = -self.speed_y

    def stop_moving(self):
        self.dy = 0

    def bind_key_up(self, key):
        self.getscreen().onkeypress(self.move_up, key)
        self.getscreen().onkey(self.stop_moving, key)

    def bind_key_down(self, key):
        self.getscreen().onkeypress(self.move_down, key)
        self.getscreen().onkey(self.stop_moving, key)


class Playfield(Turtle):
    def __init__(self, width, height, bgcolor='black'):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.up()
        # self.getscreen().setup(width, height)
        self.getscreen().bgcolor(bgcolor)
        self.border_x = width - 50
        self.border_y = height - 50
        self.create_border()
        self.getscreen().listen()
        self.mainloop = self.getscreen().mainloop

    def create_border(self):
        pass


if __name__ == '__main__':
    window = Playfield(1200, 800)
    player_1 = Player(-600, 0)
    player_2 = Player(600, 0)
    player_3 = Player(0, 400)
    player_4 = Player(0, -400)
    print(player_1.name)
    print(player_2.name)
    print(player_3.name)
    print(player_4.name)
    window.mainloop()

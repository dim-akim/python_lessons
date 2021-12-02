from graph.graph import *


def main():
    house = draw_house(200, 200, 300, 300)

    def move_left(event):
        for i in house:
            moveObjectBy(i, -5, 0)

    def move_right(event):
        for i in house:
            moveObjectBy(i, 5, 0)

    onKey('Left', move_left)
    onKey('Right', move_right)

    run()


def draw_house(x, y, width, height):
    wall_x = x
    wall_y = y
    wall_width = width
    wall_height = height * 2 // 3
    wall = draw_wall(wall_x, wall_y, wall_width, wall_height)

    roof_x = x
    roof_y = y
    roof_width = width
    roof_height = height // 3
    roof = draw_roof(roof_x, roof_y, roof_width, roof_height)

    window_x = x + width // 2
    window_y = y + wall_height // 2
    window_radius = wall_height // 4
    window = draw_window(window_x, window_y, window_radius)

    return wall, roof, window


def draw_wall(x, y, width, height):
    brushColor('green')
    return rectangle(x, y, x+width, y+height)


def draw_roof(x, y, width, height):
    brushColor('blue')
    return polygon([(x, y), (x+width, y), (x+width//2, y-height)])


def draw_window(x, y, radius):
    brushColor('white')
    return circle(x, y, radius)


main()

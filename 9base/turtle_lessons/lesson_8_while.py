import turtle


joe = turtle.Turtle()
joe.pensize(4)
joe.speed(2)
joe.shape('turtle')

line = 200

def draw_fence(height, width):
    n = 0  # Счётчик, в который мы будем записывать количество нарисованных сторон
    while n < 10:  # Пока значение n будет меньше 4, повторяй следующие команды:
        # ИТЕРАЦИЯ - одно повторение цикла
        joe.forward(line)
        joe.right(36)
        n = n + 1  # Увеличить счётчик на 1

turtle.done()

import turtle
from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def draw_circle(size):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    draw_circle(size + 5)
    turtle.bgcolor('black')
    turtle.speed('fastest')
    turtle.pensize(4)

def draw_circle(size, angle, shift):
    turtle.pencolor(next(colors))
    turtle.bgcolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)

turtle.bgcolor('black')
turtle.speed('fastest')
turtle.pensize(4)
# draw_circle(30)
draw_circle(30, 1, 10)
import turtle as t
from random import random, randint
# size = 200
# points = 4
# angle = 180 - (180 / points) #144

# t.color('red')
# t.begin_fill()
# for i in range(points):
#     t.forward(size)
#     t.right(angle)

# t.end_fill()

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

# Main code
t.Screen().bgcolor('black') 
# draw_star(5, 100, 'yellow', 0, 0)

t.hideturtle()
t.speed("fastest")
while True:
    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint(10, 50)
    ranCol = (random(), random(), random())
    ranX = randint(-300, 300)
    ranY = randint(-250, 250)
    draw_star(ranPts, ranSize, ranCol, ranX, ranY)

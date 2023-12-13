import turtle as t
from random import random, randint
def draw_planet(col,x,y,size):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


t.speed("fastest")
while True:
    ranCol = (random(),random(),random())
    ranX = randint(-300,300)
    ranY = randint(-250,250)
    size = randint(10,100)
    draw_planet(ranCol,ranX,ranY,size)
    
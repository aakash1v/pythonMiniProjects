import turtle
# turtle.bgcolor('black')
# turtle.speed('fast')
# turtle.pensize(4)
# turtle.pencolor('red')
# turtle.circle(30)

def draw_circle(size):
    turtle.pencolor('red')
    turtle.circle(size)
    # draw_circle(size)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)


x = 50
while x<100:
    draw_circle(x)
    x+=10
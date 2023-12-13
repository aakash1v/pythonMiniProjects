import turtle as t
import time
# t.shape('turtle')
t.setheading(0)
t.bgcolor('Dodger blue')

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.speed("normal")
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    for counter in range(1, 3):
        t.forward(horizontal)
        t.left(90)
        t.forward(vertical)
        t.left(90)
    t.end_fill()
    t.penup()


# t.hideturtle()
# # feet
t.goto(-100, -150)
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

# # legs
t.goto(-25, -130)
rectangle(15, 100, 'grey')
t.goto(-75, -130)
rectangle(15, 100, 'grey')

# body
t.goto(-90, -30)
rectangle(100, 150, 'red')

# # arms
t.goto(-150, 70)
rectangle(60, 15, 'grey')
t.goto(-150, 85)
rectangle(15, 60, 'grey')
t.goto(10, 70)
rectangle(60, 15, 'grey')
t.goto(55, 85)
rectangle(15, 60, 'grey')

# neck
t.goto(-50, 120)
rectangle(15, 20, 'black')

# head
t.goto(-85, 140)
rectangle(80, 50, 'pink')


# eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-55, 165)
rectangle(5, 5, 'black')
t.goto(-40, 165)
rectangle(5, 5, 'black')

t.speed('slowest')
# mouth
t.goto(-65, 145)
rectangle(40, 5, 'blue')

time.sleep(5)
rectangle(1,1,"transparent")


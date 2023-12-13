import turtle as t
import time

t.bgcolor('seashell')
t.setheading(0)
t.hideturtle()

def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.speed("fastest")
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.left(90)
        t.forward(vertical)
        t.left(90)
    t.end_fill()
    t.penup()



 # feet
t.goto(-100, -150)
rectangle(50, 20, 'blue')
t.goto(-30, -150)
rectangle(50, 20, 'blue')

# # legs
t.goto(-25, -130)
rectangle(15, 100, 'red')
t.goto(-75, -130)
rectangle(15, 100, 'red')

# body
t.goto(-90, -30)
rectangle(100, 150, 'blue')

# # arms
t.goto(-150, 70)
rectangle(60, 15, 'yellow')
t.goto(-150, 85)
rectangle(15, 60, 'yellow')
t.goto(10, 70)
rectangle(60, 15, 'yellow')
t.goto(55, 85)
rectangle(15, 60, 'yellow')

# neck
t.goto(-50, 120)
rectangle(15, 20, 'brown')

# head
t.goto(-85, 140)
rectangle(80, 50, 'pink')


# eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-55, 165)
rectangle(5, 5, 'black')
t.goto(-45, 160)
rectangle(5, 5, 'black')

t.speed('slowest')
# mouth
t.goto(-65, 145)
t.right(5)
rectangle(40, 5, 'black')

# hands
t.goto(-155, 130)
rectangle(25, 25, 'green')
t.goto(-147, 140)
rectangle(10, 15, t.bgcolor())
t.goto(50, 130)
rectangle(25, 25, 'green')
t.goto(58, 140)
rectangle(10, 15, t.bgcolor())

time.sleep(5)
rectangle(1,1,"transparent")

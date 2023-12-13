import turtle as t
import time

t.bgcolor('seashell')
t.setheading(0)
t.hideturtle()

def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.speed("fast")
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.left(90)
        t.forward(vertical)
        t.left(90)
    t.end_fill()
    t.penup()

def arm(color):
    t.pendown()
    t.begin_fill()
    t.color(color)
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(10)
    t.end_fill()
    t.penup()
    t.setheading(0)

# legs
t.goto(25,-150)
rectangle(30,100,"brown")
t.goto(-25,-150)
rectangle(30,100,"brown")

# body
t.goto(-70,-50)
rectangle(160,140,"grey")

# arms_right
t.goto(90,50)
rectangle(60,20,"red")
t.setheading(90)
t.goto(150,70)
rectangle(60,20,"red")

# arm_left
t.goto(-70,50)
t.setheading(180)
rectangle(60,20,"red")
t.setheading(90)
t.goto(-130,-10)
rectangle(60,20,"red")

# head
t.goto(50,90)
rectangle(60,80,"thistle")

# eye
t.goto(10,120)
rectangle(10,10,"black")
t.goto(30,120)
rectangle(10,10,"black")

time.sleep(5)

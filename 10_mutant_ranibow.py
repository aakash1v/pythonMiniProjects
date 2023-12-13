import turtle as t 
import random

def inside_window():
    left_limit = (-t.window_width() / 2) + 100
    right_limit = (t.window_width() / 2) - 100
    top_limit = (t.window_height() / 2) - 100
    bottom_limit = (-t.window_height() / 2) + 100
    (x, y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside

def get_turn_size():
    turn_size = input('Enter turn size (wide, square, narrow): ')
    return turn_size

def move_turtle(line_length, turn_size):
    pen_colors = ['red', 'orange', 'yellow', 'green', \
    'blue', 'purple']
    t.pencolor(random.choice(pen_colors))
    if inside_window():
        if turn_size == 'wide':
            angle = random.randint(120, 150)
        elif turn_size == 'square':
            angle = random.randint(80, 90)
        else:
            angle = random.randint(20, 40)
            t.right(angle)
            t.forward(line_length)
    else:
        t.backward(line_length)


# main
t.colormode(255)
red = random.randint(0, 255)
blue = random.randint(0,255)
green = random.randint(0, 255)
t.pencolor(red, green, blue)
# t.circle(80)

# you can use function for this too
line_length = 100
line_width = 30
turn_size = 100
t.pensize(line_width)
while True:
    move_turtle(line_length, turn_size)
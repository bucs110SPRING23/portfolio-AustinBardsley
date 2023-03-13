import random
import turtle

my_turtle = turtle.Turtle()
turtle.setup(width=800, height=800, startx=0, starty=0)
my_turtle.speed(0)
y_range = turtle.window_height()/2
x_range = turtle.window_width()/2

while abs(my_turtle.xcor()) < x_range and abs(my_turtle.ycor()) < y_range:
    heads_tails = int(random.randrange(2))
    if heads_tails == 0:
        my_turtle.left(90)
        my_turtle.forward(50)
    else:
        my_turtle.right(90)
        my_turtle.forward(50)

 

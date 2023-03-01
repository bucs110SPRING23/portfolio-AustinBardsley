import random
import turtle

my_turtle = turtle.Turtle()
print(turtle.screensize())
while my_turtle.xcor() <= 400 and my_turtle.ycor() <= 300:
    heads_tails = int(random.randrange(2))
    if heads_tails == 0:
        my_turtle.left(90)
        my_turtle.forward(50)
    else:
        my_turtle.right(90)
        my_turtle.forward(50)


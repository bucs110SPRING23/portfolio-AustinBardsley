import random
import turtle

my_turtle = turtle.Turtle()
turtle.setup(width=800, height=800, startx=0, starty=0)

while -400 <=my_turtle.xcor() <= 400 and -400<= my_turtle.ycor() <= 400:
    heads_tails = int(random.randrange(2))
    if heads_tails == 0:
        my_turtle.left(90)
        my_turtle.forward(50)
    else:
        my_turtle.right(90)
        my_turtle.forward(50)
    print(my_turtle.position())

 

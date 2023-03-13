import turtle

sides = int(input("Enter Number of Sides: "))
length = float(input("Enter Side Length: "))
my_turtle = turtle.Turtle()
my_turtle.color("red")
my_turtle.shape("turtle")
my_turtle.speed(0)
for _ in range (sides):
    my_turtle.fd(length)
    my_turtle.left(360/sides)
turtle.exitonclick()
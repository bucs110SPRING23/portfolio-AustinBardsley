import turtle

sides = int(input("Enter Number of Sides: "))
length = float(input("Enter Side Length: "))
my_turtle = turtle.Turtle()
my_turtle.color("red")
my_turtle.shape("turtle")
for i in range (sides):
    my_turtle.fd(length)
    my_turtle.left(180-((sides-2)*180/sides))
turtle.exitonclick()
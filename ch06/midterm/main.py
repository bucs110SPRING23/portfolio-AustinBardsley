import turtle

def make_turtle_list(num_turtles):
    """
    takes an integer(n) and creates a list of n strings named turtle(n)
    args: int
    return: turtlelist
    """
    turtlelist = []
    for i in range (num_turtles):
        name = "turtle"+ str(i)
        turtlelist.append(name)
    return turtlelist

def draw_circles(numcircles):
    """
    draws concentric circles of varying colors
    can be revised to change circle size and color
    args: numdots
    return: True
    """
    for i in range(numcircles):
        turtle.dot(((numcircles-i)*50),(0,0,((numcircles-i)*15)))

def draw_polygon(numsides,sidelength,pen):
    """
    draws a polygon starting and ending at the start position
    args:int,int,str
    return: True
    """
    for _ in range(numsides):
        pen.left(360/numsides)
        pen.fd(sidelength)
        
def main():
    wn = turtle.getscreen()
    wn.screensize(800,800 ,"black")
    wn.colormode(255)
    template = turtle.Turtle()
    template.color("cyan")
    template.pensize(2)
    template.ht()
    template.speed(0)

    numcircles = 13
    draw_circles(numcircles)
    
    num_turtles = 16
    turtlelist = make_turtle_list(num_turtles)
    
    #Main Drawing Section
    for i,obj in enumerate(turtlelist):
        obj = template.clone()
        obj.seth(360*(i/num_turtles))

        sidelength = 110
        numsides = 8
        draw_polygon(numsides,sidelength,obj)
        
        obj.color("white")
        obj.pensize(.5)
        sidelength = 60
        draw_polygon(numsides,sidelength,obj)
    turtle.exitonclick()

main()
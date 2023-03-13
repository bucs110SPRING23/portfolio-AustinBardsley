import turtle
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
# Race 1

x = random.randrange(1,200)
michelangelo.forward(x)
y=random.randrange(1,200)
leonardo.forward(y)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Race 2
for _ in range(70):
    x = random.randrange(1,10)
    michelangelo.forward(x)
    y=random.randrange(1,10)
    leonardo.forward(y)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()

# PART B - complete part B here

pygame.init()
while 1:
    pygame.event.get()
    window = pygame.display.set_mode()
    window.fill("yellow")
    num_sides = [3,4,6,20,100,360]
    side_length = 200
    xpos = 720
    ypos = 500
    for m in (num_sides):
        points = []
        for i in range(m):
            angle = 360/m
            radians = math.radians(angle*i)
            x = xpos+side_length*math.cos(radians) 
            y = ypos+side_length*math.sin(radians)
            points.append([x,y])
        
        pygame.draw.polygon(window, "teal", points)
        pygame.display.flip()
        pygame.time.wait(1000)
        window.fill("yellow")
        pygame.display.flip()
    break





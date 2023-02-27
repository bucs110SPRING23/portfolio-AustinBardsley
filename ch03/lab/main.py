import pygame
import random

pygame.init()
while 1:
    pygame.event.get()
    window = pygame.display.set_mode([800,800])
    width = pygame.display.get_window_size()[0]
    height = pygame.display.get_window_size()[1]
    window.fill("teal")
    pygame.draw.circle(window, "black" ,(width/2 , height/2), height/2)
    pygame.draw.circle(window, "yellow" ,(width/2 , height/2), height/2-3)
    pygame.draw.line(window, "black", ((width/2), 0) , ((width/2),height))
    pygame.draw.line(window, "black", ((width/2 - height/2), height/2) , ((width/2 + height/2),height/2))
    pygame.draw.line(window, "black", ((width/2 - height/2), 0) , ((width/2 - height/2),height))
    pygame.draw.line(window, "black", ((width/2 + height/2), 0) , ((width/2 + height/2),height))
    pygame.display.flip()
    pygame.time.wait(1000)
    for _ in range (10):
        x = random.randrange (0, width)
        y = random.randrange (0, height)
        center_x = width/2
        center_y = height/2
        if (((x-center_x)**2)+((y-center_y)**2))**(1/2) <= height/2:
            pygame.draw.circle (window, "black", (x,y), 7)
            pygame.draw.circle (window, "green", (x,y), 5)
        else:
            pygame.draw.circle (window, "black", (x,y), 7)
            pygame.draw.circle (window, "red", (x,y), 5)
        pygame.display.flip()
        pygame.time.wait(500)       
    break

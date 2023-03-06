import pygame
import random

pygame.init()
done = False
color_choice = "red"
window = pygame.display.set_mode([800,800])
width = pygame.display.get_window_size()[0]
height = pygame.display.get_window_size()[1]
red_score = 0
blue_score = 0
center_x = width/2
center_y = height/2
color_choice = []
while not done:
    pygame.event.get()
    if color_choice == "red" or "blue":
        
        pygame.draw.circle(window, "black" ,(width/2 , height/2), height/2)
        pygame.draw.circle(window, "yellow" ,(width/2 , height/2), height/2-3)
        pygame.draw.line(window, "black", ((width/2), 0) , ((width/2),height))
        pygame.draw.line(window, "black", ((width/2 - height/2), height/2) , ((width/2 + height/2),height/2))
        pygame.draw.line(window, "black", ((width/2 - height/2), 0) , ((width/2 - height/2),height))
        pygame.draw.line(window, "black", ((width/2 + height/2), 0) , ((width/2 + height/2),height))
        pygame.display.flip
        for _ in range (10):
            x = random.randrange (0, width)
            y = random.randrange (0, height)
            pygame.draw.circle (window, "black", (x,y), 7)
            pygame.draw.circle (window, "red", (x,y), 5)
            if (((x-center_x)**2)+((y-center_y)**2))**(1/2) <= height/2:
                red_score += 1
            pygame.display.flip()
            pygame.time.wait(500)
            x = random.randrange (0, width)
            y = random.randrange (0, height)
            pygame.draw.circle (window, "black", (x,y), 7)
            pygame.draw.circle (window, "blue", (x,y), 5)
            if (((x-center_x)**2)+((y-center_y)**2))**(1/2) <= height/2:
                blue_score += 1
            pygame.display.flip()
            pygame.time.wait(500)
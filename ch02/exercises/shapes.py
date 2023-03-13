import pygame
pygame.init()
while 1:
    pygame.event.get()
    screen = pygame.display.set_mode()
    screen.fill("purple")
    pygame.draw.circle(screen,"black",[720,600],204)
    pygame.draw.circle(screen,"black",[720,350],134)
    pygame.draw.circle(screen,"black",[720,180],94)
    pygame.draw.circle(screen,"white",[720,600],200)
    pygame.draw.circle(screen,"white",[720,350],130)
    pygame.draw.circle(screen,"white",[720,180],90)
    pygame.display.flip()
    pygame.time.wait(2000) 
    break


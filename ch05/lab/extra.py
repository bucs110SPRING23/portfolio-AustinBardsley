import pygame

pygame.init()
while 1:
    pygame.event.get()
    points = [(0,2),(1,5),(7,18),(24,36)]
    wn = pygame.display.set_mode((800,800))
    wn.fill("white")
    pygame.draw.lines(wn,"black",False,points)
    
    
    display = pygame.transform.flip(wn, False, True)
    #wn.blit(display,(0,0))
    width, height = wn.get_size()
    new_display = pygame.transform.scale(wn, (width * 8, height * 8))
    wn.blit(new_display,(0,800))
    pygame.display.flip()
    pygame.time.wait(2000)
    break



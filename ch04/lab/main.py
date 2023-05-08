import pygame
import random

pygame.init()
while 1:
    pygame.event.get()
    window = pygame.display.set_mode([800,800])
    width = pygame.display.get_window_size()[0]
    height = pygame.display.get_window_size()[1]
    red_score = 0
    blue_score = 0
    color_choice = []
    font = pygame.font.Font(None, 48) 
    done = False
    window.fill("white")
    red_hitbox = pygame.Rect(100,400,200,200)
    blue_hitbox = pygame.Rect(500,400,200,200)
    text = font.render("Click the color you predict to win:", True, "black")
    window.blit(text, (100,height/2-200))
    pygame.draw.rect(window,"red",red_hitbox)
    pygame.draw.rect(window,"blue",blue_hitbox)
    pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if red_hitbox.collidepoint(event.pos):
                    color_choice = "red"
                elif blue_hitbox.collidepoint(event.pos):
                    color_choice = "blue"
                
        if color_choice == "red" or color_choice == "blue":
            window.fill("teal")
            pygame.draw.circle(window, "black" ,(width/2 , height/2), height/2)
            pygame.draw.circle(window, "yellow" ,(width/2 , height/2), height/2-3)
            pygame.draw.line(window, "black", ((width/2), 0) , ((width/2),height))
            pygame.draw.line(window, "black", ((width/2 - height/2), height/2) , ((width/2 + height/2),height/2))
            pygame.draw.line(window, "black", ((width/2 - height/2), 0) , ((width/2 - height/2),height))
            pygame.draw.line(window, "black", ((width/2 + height/2), 0) , ((width/2 + height/2),height))
            pygame.display.flip
            pygame.time.wait(1000)
            for _ in range (10):
                x = random.randrange (0, width)
                y = random.randrange (0, height)
                pygame.draw.circle (window, "black", (x,y), 7)
                pygame.draw.circle (window, "red", (x,y), 5)
                if (((x-width/2)**2)+((y-height/2)**2))**(1/2) <= height/2:
                    red_score += 1
                pygame.display.flip()
                pygame.time.wait(800)
                x = random.randrange (0, width)
                y = random.randrange (0, height)
                pygame.draw.circle (window, "black", (x,y), 7)
                pygame.draw.circle (window, "blue", (x,y), 5)
                if (((x-width/2)**2)+((y-height/2)**2))**(1/2) <= height/2:
                    blue_score += 1
                pygame.display.flip()
                pygame.time.wait(800)
            window.fill("white")
            text = font.render("RED:", True, "black")
            window.blit(text, (25,50))
            text = font.render(str(red_score), True, "black")
            window.blit(text, (120,50))
            text = font.render("BLUE:", True, "black")
            window.blit(text, (width-150,50))
            text = font.render(str(blue_score), True, "black")
            window.blit(text, (width-40,50))

            if red_score > blue_score:
                if color_choice == "red":
                    text = font.render("Red Wins! - You Guessed Correctly!", True, "black")
                    window.blit(text, (100,height/2))
                else:
                    text = font.render("Red Wins! - You Guessed Incorrectly :(", True, "black")
                    window.blit(text, (100,height/2))
            elif red_score < blue_score:
                if color_choice == "blue":
                    text = font.render("Blue Wins! - You Guessed Correctly!", True, "black")
                    window.blit(text, (100,height/2))
                else:
                    text = font.render("Blue Wins! - You Guessed Incorrectly :(", True, "black")
                    window.blit(text, (100,height/2))    
            else:
                text = font.render("It's a Tie!", True, "black")
                window.blit(text, (width/2-100,height/2))
            pygame.display.flip()
            pygame.time.wait(2000)
            break
    break
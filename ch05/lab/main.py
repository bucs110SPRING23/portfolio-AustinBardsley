import pygame

def threenp1(n):
    """
    returns the number of times it takes for an 
    integer to return to 1 with the 3np1 sequence
    args: n
    return: int
    """
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    """
    creates a dictionary of 3np1 values up to the integer 'upper_limit'
    args: upperlimit
    return: dict
    """
    threenp1_dict = {}
    for i in range(2, upper_limit+1):
        threenp1_dict[i] =  threenp1(i)
    return threenp1_dict

def graph_coordinates(n):
    """graphs lines between each consecutive pair of coordinates 
    in a given dictionary. Also displays coordinate pair with greatest output
    args: n
    return: dict
    """
    
    if len(n.items()) >= 2:
        points = list(n.items())
    wn = pygame.display.set_mode((800,800))
    wn.fill("white")
    max_so_far = (0,0)
    for k,v in points:
        if v > max_so_far[1]:
            max_so_far = (k,v)
    pygame.draw.lines(wn,"black",False,points)
    
    #flipping and scaling screen
    flipped = pygame.transform.flip(wn, False, True)
    wn.blit(flipped, (0,0))
    width, height = wn.get_size()
    scaled = pygame.transform.scale(flipped, (width * 7, height * 5))
    wn.blit(scaled, (0,-3200))

    #font stuff
    font = pygame.font.Font(None, 50)
    msg = font.render(str(max_so_far), True, "blue")
    wn.blit(msg, (10,10))
    pygame.display.flip()
    pygame.time.wait(2000)
    
def main():
    upper_limit = 100
    threenp1_dict  = threenp1range(upper_limit)
    pygame.init()
    while 1:
        pygame.event.get()
        graph_coordinates(threenp1_dict)
        break
main()
import pygame
import math   
from robot3 import Robot  

# class Wall(pygame.Surface):
#     def __init__(self, size=(40,40), color=(10,20,100)):
#         super().__init__(size)
#         pygame.draw.rect(self, color, (0,0,size[0],size[1]))

# w1 = Wall(size=(100,20))



def main(parent):
    r1 = Robot()
    clock = pygame.time.Clock()   
    parent.fill((255, 255, 255))   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONUP:
                r1.set_target(pygame.mouse.get_pos())
        
        # parent.blit(w1, (10,10))
        r1.update()        
        parent.fill((255, 255, 255))
        r1.draw(parent)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))    
    main(screen)
import pygame
import math   
import numpy as np
from robot3 import Robot  

class Obstacles(pygame.Surface):
    def __init__(self, size=(40,40), color=(10,20,100)):
        super().__init__(size, pygame.SRCALPHA, 32)
        self.convert_alpha()
        # Draw border
        pygame.draw.polygon(self, color, ((5,0), (0,0), (0,size[1]), (size[0], size[1]), (size[0], 0), (5,0), (5,5), (size[0]-5,5), (size[0]-5, size[1]-5), (5,size[1]-5)),2)
        pygame.draw.rect(self, color, (120,20,20,400), 2)
        pygame.draw.rect(self, color, (120,419,300,40), 2)
        pygame.draw.rect(self, color, (221,150,380,30), 2)
        pygame.draw.rect(self, color, (600,150,20,430), 2)

        self.as_pixels = np.empty(size)

    def get_pixels(self):
        pixels = pygame.surfarray.pixels2d(self)
        self.as_pixels = np.copy(pixels)
        pixels.close()
        return self.as_pixels



def main(parent):
    obs = Obstacles(size=(parent.get_size()))
    # a = obs.get_pixels()
    # pixels = pygame.surfarray.pixels2d(obs)
    # pixels.close()
    # print(pixels[50,50])
    r1 = Robot()
    r1.position = (50,50)
    r1.angular_velocity = 1
    r1.velocity.x = 2
    r2 = Robot(color=(0,0,255))
    r2.position = r2.target = pygame.Vector2(750,500)
    r2.angular_velocity = 1
    r2.velocity.x = 2

    clock = pygame.time.Clock()   
    parent.fill((255, 255, 255))
    targets = ((60, 460),(150,500),(440,500),(480,400),(180,200),(180,100),(620,100),(700,150),(700,550))
    lst_targets = iter(targets)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONUP:
                # r1.set_target(pygame.mouse.get_pos())
                print(obs.get_at(pygame.mouse.get_pos()))
        
        # parent.blit(w1, (10,10))
        if r1.idle:
            try:
                r1.set_target(next(lst_targets))
            except StopIteration:
                pass
        r1.update()  
        r2.update()      
        parent.fill((255, 255, 255))
        pygame.draw.lines(parent, (0,0,255),False, targets)
        parent.blit(obs, (0,0))
        r1.draw(parent)
        r2.draw(parent)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))    
    main(screen)
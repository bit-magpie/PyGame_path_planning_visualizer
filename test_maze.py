import pygame
import math   
import numpy as np
from robot3 import Robot  

class Grid(object):
    def __init__(self, size=(800,600), u_length=40):
        self.h_units = int(size[0]/u_length)
        self.v_units = int(size[1]/u_length)
        self.unit_length = u_length
        self.size = size
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        self.surface.convert_alpha()

        self.obstacles = list()
        self.targets = list()
        self.cells = list()
        for i in range(self.h_units):
            self.cells.append([[0, self.get_cell_center(i,j)] for j in range(self.v_units)])

    def get_cell_center(self, i, j):
        return int(i*self.unit_length + self.unit_length/2), int(j*self.unit_length + self.unit_length/2)

    def set_obstacles(self):
        for obs in self.obstacles:
            self.cells[obs[0]][obs[1]][0] = 100

    def get_surface(self):
        self.set_obstacles()
        
        for obs in self.obstacles:
            pygame.draw.rect(self.surface, (10,20,100), self.get_rect(obs))

        for i in range(self.h_units):
            for j in range(self.v_units):
                if self.cells[i][j][0] == 0:
                    pygame.draw.rect(self.surface, (10,20,100), self.get_rect((i,j)), 1)

        return self.surface

    def set_target(self, position, robot=0):
        self.targets.append([robot, position])
        for trg in self.targets:
            pygame.draw.rect(self.surface, (255,255,0), self.get_rect(trg[1]))
            pygame.draw.circle(self.surface, (255,0,0), self.get_center(trg[1]), int(self.unit_length/2) - 2, 4)

    def get_center(self, cell):
        return self.cells[cell[0]][cell[1]][1]

    def get_rect(self, cell):
        cell_center = self.get_center(cell)
        return (cell_center[0] - self.unit_length/2, cell_center[1] - self.unit_length/2, self.unit_length, self.unit_length)


def main(parent):
    g = Grid()
    g.obstacles = [[4,1], [4,2],[4,3],[4,4],[4,5],[4,6],[10,3],[11,3],[12,3],[13,3],[14,3],[11,9],[11,10],[11,11],[11,12]]
    sfr_grid = g.get_surface()
    g.set_target((18,13), robot=0)

    r1 = Robot()
    r1.position = (50,50)
    r1.angular_velocity = 1
    r1.velocity.x = 2

    targets = [(2,1),(3,2),(3,7),(12,8),(18,13)]
    # targets = ((60, 460),(150,500),(440,500),(480,400),(180,200),(180,100),(620,100),(700,150),(700,550))
    lst_targets = iter([g.get_center(t) for t in targets])

    clock = pygame.time.Clock() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
        
        if r1.idle:
            try:
                r1.set_target(next(lst_targets))
            except StopIteration:
                pass
        
        r1.update()
        parent.fill((255, 255, 255))
        parent.blit(sfr_grid, (0,0))
        r1.draw(parent)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))    
    main(screen)
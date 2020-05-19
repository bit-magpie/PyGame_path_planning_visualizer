import pygame
import math   
import numpy as np
from robot3 import Robot
from a_star import astar   
from planner import Planner
from grid import Grid


def main(parent):
    g = Grid()
    # g.obstacles = [[4,1],[4,2],[4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[9,6],[10,6],[11,6],[12,6],[13,6],[14,6],[11,7],[11,8],[11,9],[11,10],[11,11],[11,12],[11,13]]
    # g.obstacles = [[4,1], [4,2],[4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[10,3],[11,3],[12,3],[13,3],[14,3],[11,9],[11,10],[11,11],[11,12],[11,13]]
    # g.obstacles = [[3,12], [4,12],[5,12],[6,12],[13,4],[13,5],[13,6],[13,7],[13,8],[15,7],[16,7],[17,7],[16,2],[16,13],[3,4]]
    g.set_obstacles_file(path='maps/obstacles1_2.data')
    sfr_grid = g.get_surface()
    # g.set_target((18,13), robot=0)

    r1 = Robot()
    init_pos = (0,0)
    r1.position = g.get_center(init_pos)
    r1.angular_velocity = 1
    r1.velocity.x = 2
    
    d = Planner(g)
    d.find_vertices()
    # for v in d.turn_points:
    g.select_cells(d.turn_points, color=(100,255,100))
    d.get_paths()
    for path in d.connection:
        pygame.draw.line(sfr_grid, (0,0,0), g.get_center(path[0]), g.get_center(path[1]))

    targets = []
    # print(r1.position)
    # targets = [(2,1),(3,1),(3,7),(12,8),(18,13)]
    # targets = ((60, 460),(150,500),(440,500),(480,400),(180,200),(180,100),(620,100),(700,150),(700,550))
    lst_targets = iter([]) # iter([g.get_center(t) for t in targets])

    clock = pygame.time.Clock() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONUP:
                g.set_target(g.get_cell(pygame.mouse.get_pos()))
                # print(g.targets[-1])
                targets = astar(g.cost_map, g.get_cell(r1.position), g.targets[-1][1])
                # print(targets)
                lst_targets = iter([g.get_center(t) for t in targets])
        
        if r1.idle and len(targets) > 0:
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
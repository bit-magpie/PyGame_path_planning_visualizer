import pygame
import math   
import numpy as np
from robot3 import Robot
from a_star import astar   
from planner import Planner
from grid import Grid


def main(parent):
    g = Grid()
    g.set_obstacles_file(path='maps/obstacles1_3.data')
    sfr_grid = g.get_surface()

    r1 = Robot()
    init_pos = (0,0)
    r1.position = g.get_center(init_pos)
    r1.angular_velocity = 1
    r1.velocity.x = 2

    r2 = Robot(color=(0,150,0))
    init_pos2 = (3,14)
    r2.position = g.get_center(init_pos2)
    r2.set_target(g.get_center(init_pos2))
    r2.angular_velocity = 1
    r2.linear_velocity = 2

    r3 = Robot(color=(0,0,255))
    init_pos3 = (14,14)
    r3.position = g.get_center(init_pos3)
    r3.set_target(g.get_center(init_pos3))
    r3.angular_velocity = 1
    r3.linear_velocity = 3
    
    targets1 = []
    lst_targets1 = iter([])

    targets2 = []
    lst_targets2 = iter([])

    targets3 = []
    lst_targets3 = iter([])

    selected_robot = 1

    clock = pygame.time.Clock() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONUP:
                if g.get_cost(g.get_cell(pygame.mouse.get_pos())) == 0:
                    if selected_robot == 1:
                        g.set_target(g.get_cell(pygame.mouse.get_pos()))
                        targets1 = astar(g.cost_map, g.get_cell(r1.position), g.targets[-1][1])
                        lst_targets1 = iter([g.get_center(t) for t in targets1])
                    elif selected_robot == 2:
                        g.set_target(g.get_cell(pygame.mouse.get_pos()), robot=2, color=r2.color)
                        targets2 = astar(g.cost_map, g.get_cell(r2.position), g.targets[-1][1])
                        lst_targets2 = iter([g.get_center(t) for t in targets2])
                    elif selected_robot == 3:
                        g.set_target(g.get_cell(pygame.mouse.get_pos()), robot=3, color=r3.color)
                        targets3 = astar(g.cost_map, g.get_cell(r3.position), g.targets[-1][1])
                        lst_targets3 = iter([g.get_center(t) for t in targets3])

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_robot = 1
                if event.key == pygame.K_2:
                    selected_robot = 2
                if event.key == pygame.K_3:
                    selected_robot = 3

        if r1.idle and len(targets1) > 0:
            try:
                r1.set_target(next(lst_targets1))
            except StopIteration:
                pass
        
        if r2.idle and len(targets2) > 0:
            try:
                r2.set_target(next(lst_targets2))
            except StopIteration:
                pass
        
        if r3.idle and len(targets3) > 0:
            try:
                r3.set_target(next(lst_targets3))
            except StopIteration:
                pass
        
        r1.update()
        r2.update()
        r3.update()
        parent.fill((255, 255, 255))
        parent.blit(sfr_grid, (0,0))
        r1.draw(parent)
        r2.draw(parent)
        r3.draw(parent)
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))    
    main(screen)
import pygame
import math   
import numpy as np
from robot3 import Robot
from planner import Planner
from grid import Grid

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position[0] == other.position[0] and self.position[1] == other.position[1]

class AStar(object):
    def __init__(self, maze, start, end):
        self.maze = maze
        self.open_list = []
        self.closed_list = []
        self.is_goal = False
        
        self.start_node = Node(None, start)
        self.start_node.g = self.start_node.h = self.start_node.f = 0
        self.end_node = Node(None, end)
        self.end_node.g = self.end_node.h = self.end_node.f = 0
        self.open_list.append(self.start_node)

    def set_target(self, pos):
        self.end_node = Node(None, pos)

    def get_close_list(self):
        return [n.position for n in self.closed_list]

    def get_open_list(self):
        return [n.position for n in self.open_list]

    def update(self):
        if not self.is_goal:
            if len(self.open_list) > 0:

                # Get the current node
                current_node = self.open_list[0]
                print(current_node.position)
                current_index = 0
                for index, item in enumerate(self.open_list):
                    if item.f < current_node.f:
                        current_node = item
                        current_index = index

                # Pop current off open list, add to closed list
                self.open_list.pop(current_index)
                if current_node not in self.closed_list:
                    self.closed_list.append(current_node)
                print('cur: ', current_node.position, 'end: ', self.end_node.position)
                # Found the goal
                if current_node == self.end_node:
                    print('goal found')
                    path = []
                    current = current_node
                    while current is not None:
                        path.append(current.position)
                        current = current.parent
                    self.is_goal = True
                    return path[::-1] # Return reversed path
                    

                # Generate children
                children = []
                for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

                    # Get node position
                    node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                    # Make sure within range
                    if node_position[0] > (len(self.maze) - 1) or node_position[0] < 0 or node_position[1] > (len(self.maze[len(self.maze)-1]) -1) or node_position[1] < 0:
                        continue

                    # Make sure walkable terrain
                    if self.maze[node_position[0]][node_position[1]] != 0:
                        continue

                    # Create new node
                    new_node = Node(current_node, node_position)

                    # Append
                    children.append(new_node)

                # Loop through children
                for child in children:

                    # Child is on the closed list
                    for closed_child in self.closed_list:
                        if child == closed_child:
                            continue

                    # Create the f, g, and h values
                    child.g = current_node.g + 1
                    child.h = ((child.position[0] - self.end_node.position[0]) ** 2) + ((child.position[1] - self.end_node.position[1]) ** 2)
                    child.f = child.g + child.h

                    # Child is already in the open list
                    for open_node in self.open_list:
                        if child == open_node and child.g > open_node.g:
                            continue

                    # Add the child to the open list
                    if child not in self.open_list:
                        self.open_list.append(child)



def main(parent):
    g = Grid()
    g.set_obstacles_file(path='maps/obstacles1_3.data')
    sfr_grid = g.get_surface()

    # r1 = Robot()
    # init_pos = (0,0)
    # r1.position = g.get_center(init_pos)
    # r1.angular_velocity = 1
    # r1.velocity.x = 2
    trg = (16,10)
    g.set_target(trg)
    astr = AStar(g.cost_map, (0,0), trg)
    targets = []
    lst_targets = iter([])

    clock = pygame.time.Clock() 
    drw = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONUP:    
                g.set_target(g.get_cell(pygame.mouse.get_pos()))    
                astr.set_target(g.get_cell(pygame.mouse.get_pos()))
                # astr.update()
                # g.select_cells(astr.get_open_list(), color=(100,200,100))
                # g.select_cells(astr.get_close_list(), color=(200,100,100))
                # print('open: ',astr.get_open_list())
                # print('close: ',astr.get_close_list())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    drw = not drw
        
        if drw:
            astr.update()
            g.select_cells(astr.get_open_list(), color=(200,100,100))
        parent.fill((255, 255, 255))
        parent.blit(sfr_grid, (0,0))
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))    
    main(screen)
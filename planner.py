import pygame
import numpy as np
from pygame.math import Vector2

class Planner():
    def __init__(self, grid):
        self.grid = grid
        self.turn_points = []
        self.connection = []
        # self.current = current
        # self.target = target

    def find_vertices(self):
        for i in range(self.grid.h_units):
            for j in range(self.grid.v_units):
                if self.grid.cells[i][j][0] == 0:
                    obs_count = []
                    if len(obs_count) < 3:
                        for pos in self.get_neighbors((i,j)):
                            if self.grid.cells[pos[0]][pos[1]][0] == 100:
                                obs_count.append(pos)
                                    
                    if len(obs_count) == 1:
                        if (abs(i - obs_count[0][0]) + abs(j - obs_count[0][1])) == 2:
                            self.turn_points.append((i,j))

    def get_neighbor_pos(self, cell):
        if (cell[0] == 0 or cell[0] == self.grid.h_units - 1 or cell[1] == 0 or cell[1] == self.grid.v_units - 1):
            if (cell[0] == 0 and cell[1] == 0):
                return [(1,0), (1,1), (0,1)]
            elif (cell[0] == self.grid.h_units - 1 and cell[1] == 0):
                return [(0,1), (-1,1), (-1,0)]
            elif (cell[0] == 0 and cell[1] == self.grid.v_units - 1):
                return [(0,-1), (1,-1), (1,0)]
            elif (cell[0] == self.grid.h_units - 1 and cell[1] == self.grid.v_units - 1):
                return [(-1,0), (-1,-1), (0,-1)]
            elif (cell[0] == 0):
                return [(0,-1), (1,-1), (1,0), (1,1), (0,1)]
            elif (cell[1] == 0):
                return [(1,0), (1,1), (0,1), (-1,1), (-1,0)]
            elif (cell[0] == self.grid.h_units - 1):
                return [(0,1), (-1,1), (-1,0), (-1,-1), (0,-1)]
            elif (cell[1] == self.grid.v_units - 1):
                return [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0)]
        else:
            return [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
            # return [(-1,-1),  (1,-1), (1,1), (-1,1)]

    def get_neighbors(self, cell):
        return [tuple(np.array(cell) + np.array(c)) for c in self.get_neighbor_pos(cell)]

    def get_paths(self):
        t_points = self.turn_points
        for point in t_points:
            for other in t_points:
                if point != other:
                    diff_vector = (Vector2(other) - Vector2(point))
                    length = int(diff_vector.length())
                    no_crossings = True
                    for i in range(length+1):
                        seg = i*(1/length)*diff_vector + point
                        cross = (round(seg.x),round(seg.y))
                        if self.grid.cells[cross[0]][cross[1]][0]>0:
                            no_crossings = False
                            break
                    
                    if no_crossings:
                        self.connection.append([point, other])
                    if point in t_points:
                        t_points.remove(point)

        print(len(self.connection))
    def get_shortest(self):
        pass
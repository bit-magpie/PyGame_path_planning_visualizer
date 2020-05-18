import pygame
import numpy as np

class Planner():
    def __init__(self, grid):
        self.grid = grid
        self.turn_points = []
        # self.current = current
        # self.target = target

    def find_vertices(self):
        for i in range(self.grid.h_units):
            for j in range(self.grid.v_units):
                if self.grid.cells[i][j][0] == 0:
                    obs_count = []
                    if len(obs_count) < 2:
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

    def get_shortest(self):
        pass
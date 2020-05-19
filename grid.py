import pygame

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
        self.cost_map = [[0 for _ in range(self.v_units)] for _ in range(self.h_units)] 
        self.cells = list()     
        for i in range(self.h_units):
            self.cells.append([[0, self.get_cell_center(i,j)] for j in range(self.v_units)])

    def redraw_all(self):
        self.surface.fill((255,255,255))
        _ = self.get_surface()

    def get_cell_center(self, i, j):
        return int(i*self.unit_length + self.unit_length/2), int(j*self.unit_length + self.unit_length/2)

    def set_obstacles(self):
        for obs in self.obstacles:
            self.cells[obs[0]][obs[1]][0] = 100
            self.cost_map[obs[0]][obs[1]] = 100

    def get_surface(self):
        self.set_obstacles()
        
        for obs in self.obstacles:
            pygame.draw.rect(self.surface, (10,20,100), self.get_rect(obs))

        for i in range(self.h_units):
            for j in range(self.v_units):
                if self.cells[i][j][0] == 0:
                    pygame.draw.rect(self.surface, (220,220,220), self.get_rect((i,j)), 1)

        return self.surface

    def set_target(self, position, robot=0, color=(255,0,0)):
        for target in self.targets:
            if target[0] == robot:
                self.targets.remove(target)
        # if self.cells[position[0]][position[1]][0] == 0:
        self.targets.append([robot, position, color])
        self.redraw_all()
        for trg in self.targets:
            pygame.draw.rect(self.surface, (250,250,150), self.get_rect(trg[1]))
            pygame.draw.circle(self.surface, trg[2], self.get_center(trg[1]), int(self.unit_length/2) - 2, 4)

    def select_cells(self, cells, color=(50,50,100)):        
        self.redraw_all()
        for cell in cells:
            pygame.draw.rect(self.surface, color, self.get_rect(cell))

    def get_cost(self, position):
        return self.cells[position[0]][position[1]][0]

    def get_center(self, cell):
        return self.cells[cell[0]][cell[1]][1]

    def get_cell(self, pixel):
        return (int(pixel[0]/self.unit_length), int(pixel[1]/self.unit_length))

    def get_rect(self, cell):
        cell_center = self.get_center(cell)
        return (cell_center[0] - self.unit_length/2, cell_center[1] - self.unit_length/2, self.unit_length, self.unit_length)

    def set_obstacles_file(self, path='maps/obstacles.data'):
        file_obj  = open(path, "r") 
        data = []
        for line in file_obj.readlines():
            cord = line.split(',')
            data.append([int(cord[0]),int(cord[1])])
        self.obstacles = data

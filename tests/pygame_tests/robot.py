import pygame
import math

class Robot(pygame.Surface):
    def __init__(self, parent, size=(40,40), color=(255,0,0)):
        # super().__init__(size)
        super().__init__(size, pygame.SRCALPHA, 32)
        self.convert_alpha()
        pygame.draw.circle(self, color, (int(size[0]/2),int(size[1]/2)), 20)
        pygame.draw.polygon(self, (230, 230, 230), ((10,8),(10,32),(35,20)))
        # im_obj = pygame.image.load('pygame_tests/circ.png')
        # self.blit(im_obj, (0,0))
        self.center = self.get_rect().center
        self.parent = parent
        self.position = (0,0)
        self.angle = 0
        self.linear_speed = 10
        self.angular_speed = 1
    
    def set_movement(self, linear=0, angular=0):
        self.angle += angular
        speedx = math.cos(self.angle * math.pi/180) * linear
        speedy = math.sin(self.angle * math.pi/180) * linear
        self.position = (self.position[0] + speedx, self.position[1] + speedy)
        self.update_position()

    def update_position(self):
        rotated = pygame.transform.rotate(self, -self.angle)
        self.parent.blit(rotated, (self.position[0] - self.center[0], self.position[1] - self.center[1]))

    def draw_trajectory(self):
        coordinates = []
        position = self.position
        angle = self.angle
        # print(pygame.display.get_surface().get_size())
        # while (position[0] > 0 or position[0] < w or position[1] > 0 or position[1] < h):
        for _ in range(500):
            angle += self.angular_speed
            x = math.cos(angle * math.pi/180) * self.linear_speed
            y = math.sin(angle * math.pi/180) * self.linear_speed
            position = (position[0] + x, position[1] + y)
            coordinates.append(position)

        if ( len( coordinates ) > 1 ):
            # print(coordinates)
            PINK = ( 0, 0, 255 )
            pygame.draw.lines(self.parent, PINK, False, coordinates)
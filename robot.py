import pygame
from math import sin, radians, degrees, copysign, ceil
from pygame.math import Vector2

class Robot(pygame.sprite.Sprite):
    def __init__(self, size=(40,40), color=(255,0,0)):
        super().__init__()
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (int(size[0]/2),int(size[1]/2)), 20)
        pygame.draw.polygon(self.image, (230, 230, 230), ((10,8),(10,32),(35,20)))

        self.id = 0
        self.color = color
        self.rect = self.image.get_rect()
        self.position = Vector2(self.rect.center )
        self.velocity = Vector2(1.0, 0.0)
        self.angle = 0
        self.length = self.rect[2]
        self.acceleration = 0.0
        self.angular_velocity = 1
        self.linear_velocity = 1
        self.idle = True

        self.target = self.position

    def set_target(self, position):
        self.target = Vector2(position)
        self.idle = False

    def update(self):
        diff_vector = self.target - self.position
        distance = diff_vector.length()
        if distance > 20:
            angle = -ceil(diff_vector.as_polar()[1])
            diff_angle = (angle - self.angle) %360
        else:
            angle = self.angle
            diff_angle = 0
        
        self.velocity += (self.acceleration, 0)

        if diff_angle != 0:
            self.velocity.x = 0
            self.position += self.velocity.rotate(self.angle)
            if diff_angle > 180:
                self.angle -= self.angular_velocity
            else:
                self.angle += self.angular_velocity
        else:
            self.velocity.x = self.linear_velocity
            if distance < self.velocity.x:
                self.position = self.target
                self.idle = True
            elif distance != 0:
                diff_vector.normalize_ip()
                diff_vector = diff_vector * self.velocity.x            
                self.position += diff_vector
        
    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect()
        screen.blit(rotated, self.position - rect.center) # (rect.width / 2, rect.height / 2))
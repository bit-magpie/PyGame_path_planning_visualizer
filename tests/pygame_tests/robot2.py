import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2


class Robot(pygame.sprite.Sprite):
    def __init__(self, size=(40,40), color=(255,0,0)):
        super().__init__()
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.image.convert_alpha()
        pygame.draw.circle(self.image, color, (int(size[0]/2),int(size[1]/2)), 20)
        pygame.draw.polygon(self.image, (230, 230, 230), ((10,8),(10,32),(35,20)))

        self.rect = self.image.get_rect()
        self.position = Vector2(40, 40)
        self.velocity = Vector2(1.0, 0.0)
        self.angle = 0
        self.length = self.rect[2]
        self.acceleration = 0.0
        self.angular_velocity = 1

        self.target = Vector2(500, 400)

    def set_target(self, position):
        self.target = Vector2(position)

    def update(self):
        diff_vector = self.target - self.position
        distance = diff_vector.length()
        self.angle = -diff_vector.as_polar()[1]

        self.velocity += (self.acceleration, 0)
        # self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        # if self.steering:
        #     turning_radius = 1/sin(radians(self.steering))
        #     angular_velocity = self.velocity.x / turning_radius
        # else:
        #     angular_velocity = 0
        if distance < self.velocity.x:
            self.position = self.target
        elif distance != 0:
            diff_vector.normalize_ip()
            diff_vector = diff_vector * self.velocity.x
            self.position += self.velocity.rotate(-self.angle)
            self.position += diff_vector
            # self.angle += self.angular_velocity

    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect()
        screen.blit(rotated, self.position - rect.center) # (rect.width / 2, rect.height / 2))
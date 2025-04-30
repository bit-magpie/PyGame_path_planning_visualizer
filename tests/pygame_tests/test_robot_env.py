import pygame
import math   
from pygame_tests.robot import Robot  

def main(parent):
    clock = pygame.time.Clock()   
    parent.fill((255, 255, 255))
    
    player = Robot(parent)
    player.position = (300,50)
    vel = [4, 1.5]
    player.linear_speed = vel[0]
    player.angular_speed = vel[1]

    player1 = Robot(parent, color=(0,255,0))
    player1.position = (500,200)
    vel1 = [2, 1]
    player1.linear_speed = vel1[0]
    player1.angular_speed = vel1[1] 

    player2 = Robot(parent, color=(0,0,255))
    player2.position = (150,300)
    vel2 = [3, -2]
    player2.linear_speed = vel2[0]
    player2.angular_speed = vel2[1]    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    vel[0] += 0.1
                if event.key == pygame.K_x:
                    vel[0] -= 0.1
                if event.key == pygame.K_d:
                    vel[1] += 0.1
                if event.key == pygame.K_a:
                    vel[1] -= 0.1

        # player.update()
        parent.fill((255, 255, 255))
        player.set_movement(linear=vel[0], angular=vel[1])
        player.draw_trajectory()
        player1.set_movement(linear=vel1[0], angular=vel1[1])
        player1.draw_trajectory()
        player2.set_movement(linear=vel2[0], angular=vel2[1])
        player2.draw_trajectory()
        
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))    
    main(screen)
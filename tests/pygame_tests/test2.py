import pygame
from PIL import Image, ImageDraw

img = Image.new('RGB', (50,50), color=(24,56,250))
img.save('a.png')

pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill((255,255,255))
clock = pygame.time.Clock()

im_obj = pygame.image.load('circ.png')
srf = pygame.Surface((42,42))
srf.blit(im_obj, (0,0))
# pygame.transform.rotate(im_obj, 30)

running = True

c = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False 

    screen.fill((255,255,255))
    r_img = pygame.transform.rotate(srf, -c)
    screen.blit(r_img, (c,c))
    
    pygame.display.update()
    clock.tick(60)
    c += 0.5

    if c > 500:
        c = 0
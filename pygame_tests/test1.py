import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((255,255,255))
clock = pygame.time.Clock()

# background = pygame.Surface(screen.get_size())
# background.fill((255,255,255))
# background = background.convert()
# screen.blit(background, (0, 0))

game_over = False

x, y = 20,20
x1, y1 = 20,80
xc = 1
xc2 = 2
mpos = []
iterpos = None
record = False
movecir = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            game_over = True 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True 
            elif event.key == pygame.K_r:
                record = True
            elif event.key == pygame.K_s:
                record = False
                iterpos = iter(mpos)
            elif event.key == pygame.K_m:
                movecir = True

    if record:
        mpos.append(pygame.mouse.get_pos())

    screen.fill((255,255,255))

    if movecir:
        try:
            xy = next(iterpos)
            pygame.draw.circle(screen, (255,0,0), xy, 10)
        except StopIteration:
            mpos = []
    # x += xc
    # x1 += xc2
    # screen.fill((255,255,255))
    # pygame.draw.circle(screen, (255,0,0), (x,y), 10)
    # pygame.draw.circle(screen, (0,255,0), (x1,y1), 10)
    pygame.display.update()
    clock.tick(60)

pygame.quit()




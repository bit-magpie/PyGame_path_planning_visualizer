import pygame
from grid import Grid

def save_file(data_list):
    file  = open("maps/obstacles1.data", "w+") 
    for data in data_list:
        file.write(str(data[0]) + "," + str(data[1]) + "\n")
    file.close()

def main(parent):
    g = Grid()
    # g.obstacles = read_file() 
    sfr_grid = g.get_surface()
    obstacles = []

    delete = False
    clock = pygame.time.Clock() 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_file(obstacles)
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONUP:
                pos = g.get_cell(pygame.mouse.get_pos())
                if not delete:
                    obstacles.append(pos)
                else:
                    index = obstacles.remove(pos)
                print(obstacles)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    delete = True 
                elif event.key == pygame.K_s:
                    delete = False
                
        parent.fill((255, 255, 255))
        g.select_cells(obstacles)
        parent.blit(sfr_grid, (0,0))
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 600))    
    main(screen)
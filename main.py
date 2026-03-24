from entities.pacman import Pacman
import map
import pygame

M_WIDTH = 28
M_HEIGHT = 31
TILE_SIZE = map.TEMP_WIDTH // M_WIDTH 

MAP_PIXEL_WIDTH  = TILE_SIZE * M_WIDTH
MAP_PIXEL_HEIGHT = TILE_SIZE * M_HEIGHT

WIN_SIZE_W = int(map.TEMP_WIDTH * 1.1)
WIN_SIZE_H = int(MAP_PIXEL_HEIGHT * 1.1)
WIN = pygame.display.set_mode((WIN_SIZE_W, WIN_SIZE_H))

offset_x = (WIN_SIZE_W - MAP_PIXEL_WIDTH) // 2
offset_y = (WIN_SIZE_H - MAP_PIXEL_HEIGHT) // 2

pygame.display.set_caption("Packer Test 1")

def main(win):
    clock = pygame.time.Clock()
    run = True

    game_map = map.TileMap(map.TILES)
    packer = Pacman(14, 23) 
    
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    packer.set_next_direction("up")
                if event.key == pygame.K_d:
                    packer.set_next_direction("right")
                if event.key == pygame.K_a:            
                    packer.set_next_direction("left")
                if event.key == pygame.K_s:            
                    packer.set_next_direction("down")

        packer.step(game_map)
        
        win.fill((0, 0, 0))
        
        map.draw(win, game_map)
        packer.draw(win, TILE_SIZE, offset_x, offset_y)
        
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    main(WIN)
    pygame.quit()

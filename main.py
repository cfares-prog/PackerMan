from entities.pacman import Pacman
from entities.ghost import Ghost
from ai.test_ghostAi import TestGhost
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
    
    ghosts= [ # box corners bottomLeft= 11,15 topLeft= 11, 12 topRight= 16,12 bottomRight= 16,15 
        Ghost(11, 14, "revive"),
        Ghost(11, 13, "scaredy"),
        Ghost(11, 12, "red"),
        Ghost(12, 14, "cyan"),
        Ghost(12, 13, "pink"),
        Ghost(12, 12, "orange"),
        Ghost(13, 14, "yellow"),
        Ghost(13, 13, "green"),
        Ghost(13, 12, "crimson"),
        Ghost(14, 14, "purple"),
        Ghost(14, 13, "sky"),
        Ghost(14, 12, "blue"),
        Ghost(15, 14, "gold"),
        Ghost(15, 13, "forest"),
    ]
    
    testGhost = TestGhost()
    
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
        
        for ghost in ghosts:
            testGhost.movement(game_map, packer, ghost)
            
        win.fill((0, 0, 0))
        
        map.draw(win, game_map)
        packer.draw(win, TILE_SIZE, offset_x, offset_y)
        
        for ghost in ghosts:
            ghost.draw(win, TILE_SIZE, offset_x, offset_y)
        
        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    main(WIN)
    pygame.quit()

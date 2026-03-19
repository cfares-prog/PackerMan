from pacman import pacman
import map
import pygame

WIN = pygame.display.set_mode((map.TEMP_WIDTH* 1.2, map.TEMP_WIDTH* 1.2))
pygame.display.set_caption("packer test 1")

def main(win):
    run= True
    game_map = map.TileMap(map.TILES)
    packer= pacman(1, 1, game_map, game_map.offset_x, game_map.offset_y)
    
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False

        pac_x, pac_y = packer.get_position()
        neighbors = game_map.get_neighbor(pac_x, pac_y)

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w]:
            packer.set_direction("up")
        if pressed_key[pygame.K_d]:
            packer.set_direction("right")
        if pressed_key[pygame.K_a]:            
            packer.set_direction("left")
        if pressed_key[pygame.K_s]:            
            packer.set_direction("down")

        packer.step()

        map.draw(win,game_map)
        packer.draw(win, map.TEMP_WIDTH// map.M_HEIGHT - 1, game_map)

main(WIN)

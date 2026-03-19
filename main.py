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
        map.draw(win,game_map)
        packer.move()
        packer.draw(win, map.TEMP_WIDTH// map.M_HEIGHT - 1, game_map)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w]:
            print("w")
            packer.move_up()
        if pressed_key[pygame.K_d]:
            print("d")
            packer.move_right()
        if pressed_key[pygame.K_a]:            
            print("a")
            packer.move_left()
        if pressed_key[pygame.K_s]:            
            print("s")
            packer.move_down()

main(WIN)

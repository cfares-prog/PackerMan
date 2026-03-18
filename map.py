import pygame
from sprite_loader import SpriteSheet
from enum import IntEnum

#Tiles not pixels
M_WIDTH = 28
M_HEIGHT = 31

#pixels
TEMP_WIDTH = 1080
TILE_WIDTH = 64

#temp for testing
WIN = pygame.display.set_mode((TEMP_WIDTH,TEMP_WIDTH))
pygame.display.set_caption("packer test 1")

BLACK = (0, 0, 0)
class TileSprites:
    TILE_SIZE = 8
    SCALE = 3.25

    sheet = SpriteSheet("sprites.png")
    test = sheet.get_sprite_by_grid(108,18,TILE_SIZE,TILE_SIZE)

    ver_wall = sheet.get_sprite_scaled(27,27,TILE_SIZE,TILE_SIZE,SCALE)
    hor_wall = sheet.get_sprite_scaled(117,27,TILE_SIZE,TILE_SIZE, SCALE)
    inv_hor_wall = pygame.transform.flip(hor_wall, False, True)
    inv_ver_wall = pygame.transform.flip(ver_wall, True, False)

    tleft_corner = sheet.get_sprite_scaled(9,27,TILE_SIZE,TILE_SIZE,SCALE)
    tright_corner = sheet.get_sprite_scaled(0,27,TILE_SIZE,TILE_SIZE,SCALE)
    bright_corner = sheet.get_sprite_scaled(36,27,TILE_SIZE,TILE_SIZE,SCALE)
    bleft_corner = sheet.get_sprite_scaled(45,27,TILE_SIZE,TILE_SIZE,SCALE)

    t_right = sheet.get_sprite_scaled(63, 36, TILE_SIZE, TILE_SIZE, SCALE);
    t_up = sheet.get_sprite_scaled(0, 0, TILE_SIZE, TILE_SIZE, SCALE);
    t_left = sheet.get_sprite_scaled(0, 0, TILE_SIZE, TILE_SIZE, SCALE);
    t_down = sheet.get_sprite_scaled(0, 0, TILE_SIZE, TILE_SIZE, SCALE);
    cross = sheet.get_sprite_scaled(0, 0, TILE_SIZE, TILE_SIZE, SCALE);

    coin = sheet.get_sprite_scaled(117,45,TILE_SIZE,TILE_SIZE,SCALE)
    pellet = sheet.get_sprite_scaled(135,45,TILE_SIZE,TILE_SIZE,SCALE)
    gate = sheet.get_sprite_scaled(90,54,TILE_SIZE,TILE_SIZE,SCALE)

WALL_MAPPING = {
        # Straights
        5: TileSprites.ver_wall,      
        10: TileSprites.hor_wall,     

        # Corners
        6: TileSprites.tleft_corner,  
        12: TileSprites.tright_corner,
        9: TileSprites.bright_corner, 
        3: TileSprites.bleft_corner,  

        # Dead ends 
        1: TileSprites.inv_ver_wall,      
        4: TileSprites.inv_ver_wall,      
        2: TileSprites.inv_hor_wall,      
        8: TileSprites.inv_hor_wall,      

        #Junctions
        11: TileSprites.hor_wall,
        14: TileSprites.inv_hor_wall,
        7: TileSprites.ver_wall,
        13: TileSprites.inv_ver_wall
}

class Tile(IntEnum):
    WALL  = 0
    COIN  = 1
    POWER = 2
    EMPTY = 3
    GATE  = 4

class TileMap:
    def __init__(self,tiles):
        self.tiles = tiles

    def get_tile(self, x, y):
        return self.tiles[x][y]

    def is_wall(self, x, y):
        if x < 0 or y < 0 or x >= M_HEIGHT or y >= M_WIDTH:
            return False

        return self.tiles[x][y] == Tile.WALL

    def get_neighbor(self,x, y):
        return {
                "top"   : (x, y - 1), 
                "bottom": (x, y + 1),
                "left"  : (x - 1, y),
                "right" : (x + 1, y)
                }

    #draw helper
    def get_tile_bitmask(self, row, col):
        mask = 0
        
        if self.is_wall(row - 1, col): mask += 1
        if self.is_wall(row, col + 1): mask += 2
        if self.is_wall(row + 1, col): mask += 4
        if self.is_wall(row, col - 1): mask += 8
        
        return mask

    def eat_coin(self, x, y):

        if self.tiles[x][y] == Tile.COIN:
            self.tiles[x][y] = Tile.EMPTY
            return True

        return False

TILES = [
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.POWER, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.POWER, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.WALL, Tile.GATE, Tile.GATE, Tile.WALL, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.EMPTY,Tile.EMPTY,Tile.EMPTY,Tile.EMPTY,Tile.EMPTY,Tile.EMPTY,Tile.COIN, Tile.EMPTY,Tile.EMPTY,Tile.EMPTY, Tile.WALL, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.WALL, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.COIN, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.EMPTY, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.POWER, Tile.COIN, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.EMPTY, Tile.EMPTY, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.COIN, Tile.POWER, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.COIN, Tile.WALL],
        [Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL, Tile.WALL],
        ]

def draw(win,map): 
    win.fill(BLACK)
    gap = TEMP_WIDTH// M_HEIGHT - 1


    sprites = TileSprites
    offset_x = TileSprites.TILE_SIZE * 10
    offset_y = TileSprites.TILE_SIZE * 4

    for row_index, row in enumerate(map.tiles):
        for col_index, tile in enumerate(row):

            px = col_index * gap + offset_x
            py = row_index * gap + offset_y

            if tile == Tile.WALL:
                sprite = TileSprites.test
                mask = map.get_tile_bitmask(row_index, col_index)
                
                if row_index == 0 and (col_index != 0 and col_index != M_WIDTH - 1):
                    sprite = sprites.inv_hor_wall
                elif row_index == M_HEIGHT - 1 and (col_index != 0 and col_index != M_WIDTH - 1):
                    sprite = sprites.hor_wall

                elif mask == 10:
                    if row_index >= (M_HEIGHT) // 2:
                        sprite = sprites.hor_wall
                    elif not map.is_wall(row_index + 1, col_index):
                        sprite = sprites.inv_hor_wall
                    else:
                        sprite = sprites.hor_wall

                elif  mask == 5:
                    if col_index == M_WIDTH - 1 and (row_index != 0 and row_index != M_HEIGHT -1):
                        sprite = sprites.inv_ver_wall
                    elif col_index >= (M_WIDTH - 1) // 2:
                        sprite = sprites.inv_ver_wall
                    else:
                        sprite = sprites.ver_wall

                else:
                    sprite = WALL_MAPPING.get(mask, sprites.test)

                win.blit(sprite, (px, py))

            elif tile == Tile.COIN:
               win.blit(sprites.coin,(px,py))

            elif tile == Tile.POWER:
               win.blit(sprites.pellet,(px,py))

            elif tile == Tile.GATE:
               win.blit(sprites.gate,(px,py))


    pygame.time.delay(10)
    pygame.display.update()

def main(win):
    run= True
    game_map = TileMap(TILES)

    while run:
        draw(win,game_map)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run= False
            

main(WIN)

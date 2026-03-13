import pygame
from sprite_loader import SpriteSheet
from enum import IntEnum

#Tiles not pixels
M_WIDTH = 28
M_HEIGHT = 31

#pixels
TEMP_WIDTH = 800
TILE_WIDTH = 124

#temp for testing
WIN = pygame.display.set_mode((TEMP_WIDTH,TEMP_WIDTH))
pygame.display.set_caption("packer test 1")

BLACK = (0, 0, 0)

class TileSprites:
    TILE_SIZE = 8
    SCALE = 3.25
    sheet = SpriteSheet("sprites.png")
    test = sheet.get_sprite_by_grid(0,3,TILE_SIZE,TILE_SIZE)
    hor_wall = sheet.get_sprite_scaled(27,27,TILE_SIZE,TILE_SIZE,SCALE)
    ver_wall = sheet.get_sprite_scaled(117,27,TILE_SIZE,TILE_SIZE, SCALE)
    inv_hor_wall = pygame.transform.flip(hor_wall,True,True)
    inv_ver_wall = pygame.transform.flip(ver_wall,True,True)
    tleft_corner = sheet.get_sprite_scaled(9,27,TILE_SIZE,TILE_SIZE,SCALE)
    tright_corner = sheet.get_sprite_scaled(0,27,TILE_SIZE,TILE_SIZE,SCALE)
    bright_corner = sheet.get_sprite_scaled(36,27,TILE_SIZE,TILE_SIZE,SCALE)
    bleft_corner = sheet.get_sprite_scaled(45,27,TILE_SIZE,TILE_SIZE,SCALE)
    coin = sheet.get_sprite_scaled(117,45,TILE_SIZE,TILE_SIZE,SCALE)
    pellet = sheet.get_sprite_scaled(135,45,TILE_SIZE,TILE_SIZE,SCALE)
    gate = sheet.get_sprite_scaled(90,54,TILE_SIZE,TILE_SIZE,SCALE)

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

    #helper method for draw
    def get_wall_neighbors(self, x, y):
        return {
                "top"   : self.is_wall(x, y - 1),
                "bottom": self.is_wall(x, y + 1),
                "left"  : self.is_wall(x - 1, y),
                "right" : self.is_wall(x + 1, y),
                }

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
    gap = TEMP_WIDTH// M_HEIGHT
    sprites = TileSprites

    for row_index, row in enumerate(map.tiles):
        for col_index, tile in enumerate(row):

            px = col_index * gap
            py = row_index * gap

            if tile == Tile.WALL:
                walls = map.get_wall_neighbors(row_index, col_index)

                if walls["bottom"] and walls["top"] and walls["left"] and walls["right"]:
                    pass
                
                elif walls["bottom"] and walls["right"]:
                    win.blit(sprites.tleft_corner,(px,py))

                elif walls["top"] and walls["right"]:
                    win.blit(sprites.tright_corner,(px,py))

                elif walls["bottom"] and walls["left"]:
                    win.blit(sprites.bleft_corner,(px,py))

                elif walls["top"] and walls["left"]:
                    win.blit(sprites.bright_corner,(px, py))

                #straight walls
                elif walls["top"] and walls["bottom"]:
                    if row_index > col_index:
                        win.blit(sprites.ver_wall,(px,py))
                    else:
                        win.blit(sprites.inv_ver_wall,(px,py))

                elif walls["left"] and walls["right"]:
                    if row_index > col_index:
                        win.blit(sprites.hor_wall,(px,py))
                    else:
                        win.blit(sprites.inv_hor_wall,(px,py))
                
            if tile == Tile.COIN:
               win.blit(sprites.coin,(px,py))

            if tile == Tile.POWER:
               win.blit(sprites.pellet,(px,py))

            if tile == Tile.GATE:
               win.blit(sprites.gate,(px,py))


    pygame.time.delay(10)
    pygame.display.update()

def main(win):
    run= True
    game_map = TileMap(TILES)

    while run:
        draw(win,game_map)
        for event in pygame.event.get():
            # Program Kill Switch
            if (event.type == pygame.QUIT):
                run= False
            

main(WIN)

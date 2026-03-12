import pygame
import spritesheet
from enum import IntEnum

#Tiles not pixels
M_WIDTH = 28
M_HEIGHT = 31
TEMP_WIDTH = 800
TILE_WIDTH = 124
WIN = pygame.display.set_mode((TEMP_WIDTH,TEMP_WIDTH))
pygame.display.set_caption("packer test 1")

BLACK = (0, 0, 0)

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
        return self.tiles[x][y] == Tile.WALL

    def get_neighbor(self,x, y):
        return [
                (x, y - 1), 
                (x, y + 1),
                (x - 1, y),
                (x + 1, y)
                ]

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

def draw(win,tiles):
    win.fill(BLACK)
    x = 0
    y = 0
    gap = TEMP_WIDTH// M_HEIGHT
    for row in tiles:
        for tile in row:
            pygame.draw.rect(win, tile, (y* gap, x* gap, TILE_WIDTH, TILE_WIDTH))
            y += 1
        x += 1
        y = 0

    pygame.time.delay(10)
    pygame.display.update()

def main(win):
    run= True
    game_map = TileMap(TILES)

    while run:
        draw(win,game_map.tiles)
        for event in pygame.event.get():
            # Program Kill Switch
            if (event.type == pygame.QUIT):
                run= False
            

main(WIN)

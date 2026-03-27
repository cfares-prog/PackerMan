# Requires The install of pygame package: pip install pygame
import pygame
import math
from AStarPAthFInding import algorithm


WIDTH= 600
WIN= pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algo Visuals");

RED=        (255,   0,   0)
GREEN=      (  0, 255,   0)
BLUE=       (  0,   0, 255)
WHITE=      (255, 255, 255)
BLACK=      (  0,   0,   0)
PURPLE=     (128,   0, 128)
ORANGE=     (255, 165,   0)
GREY=       (128, 128, 128)
TURQUOISE=  ( 64, 224, 208)

class Tile:
    def __init__(self, row, col, width, total_rows):
        self.row= row
        self.col= col
        self.x= row* width
        self.y= col* width
        self.color= WHITE
        self.neighbors= []
        self.width= width
        self.total_rows= total_rows
        
    def get_pos(self):
        return  self.row, self.col

    # has this Tile been looked at ?
    def is_closed(self):# yes
        return self.color == RED
    def is_open(self):# not yet
        return self.color == GREEN
    
    # is this Tile a wall ?
    def is_barrior(self):
        return self.color == BLACK
    
    # is this Tile the start or end ?
    def is_start(self):
        return self.color == ORANGE
    def is_end(self):
        return self.color == TURQUOISE
    
    # change Tile to other state
    def reset(self):
        self.color= WHITE
    def make_closed(self):
        self.color= RED
    def make_open(self):
        self.color= GREEN
    def make_barrior(self):
        self.color= BLACK
    def make_start(self):
        self.color= ORANGE
    def make_end(self):
        self.color= TURQUOISE
    def make_path(self):
        self.color= PURPLE
    
    # visual
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbors(self, grid):
        self.neighbors= []
        
        # DOWN
        if self.row < self.total_rows- 1 and not grid[self.row+ 1][self.col].is_barrior():
            self.neighbors.append(grid[self.row+ 1][self.col])
            
        # UP
        if self.row > 0 and not grid[self.row- 1][self.col].is_barrior():
            self.neighbors.append(grid[self.row- 1][self.col])
            
        # RIGHT
        if self.col < self.total_rows- 1 and not grid[self.row][self.col+ 1].is_barrior():
            self.neighbors.append(grid[self.row][self.col+ 1])
            
        # LEFT
        if self.row > 0 and not grid[self.row][self.col- 1].is_barrior():
            self.neighbors.append(grid[self.row][self.col- 1])
    
    
    def __lt__(self, other):
        return False

def make_grid(rows, width):
    grid= []
    gap= width// rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            tile= Tile(i, j, gap, rows)
            grid[i].append(tile)
    return grid

def draw_grid(win, rows, width):
    gap= width// rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i* gap), (width, i* gap))
        pygame.draw.line(win, GREY, (i* gap, 0), (i* gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    
    for row in grid:
        for tile in row:
            tile.draw(win)
    draw_grid(win, rows, width)
    pygame.time.delay(10)
    pygame.display.update()

def hget_clicked_pos(pos, rows, width):
    gap= width// rows
    y, x= pos

    row= y// gap
    col= x// gap
    return row, col

   
def main(win, width):
    ROWS= 50
    grid= make_grid(ROWS, width)
    start: Tile= None
    end: Tile= None
    run= True
    started= False
    
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            # Program Kill Switch
            if (event.type == pygame.QUIT):
                run= False
            
            # if Algorithm Started -> Halt Any Event Handling
            if started:
                continue
            
            # LEFT CLICK
            if pygame.mouse.get_pressed()[0]:
                pos= pygame.mouse.get_pos()
                row, col= hget_clicked_pos(pos, ROWS, width)
                tile: Tile= grid[row][col]
                
                if not start and tile != end:
                    start= tile
                    start.make_start()
                    # print("Start: ", start.x, start.y)
                    
                elif not end and tile != start:
                    end= tile
                    end.make_end()
                    # print("End: ", end.x, end.y)

                elif tile != end and tile != start:
                    tile.make_barrior()
                    
                # print("Left: ", pos, row, col, "Tile: ", tile.x, tile.y)
            
            # RIGHT CLICK
            elif pygame.mouse.get_pressed()[2]:
                pos= pygame.mouse.get_pos()
                row, col= hget_clicked_pos(pos, ROWS, width)
                tile: Tile= grid[row][col]
                
                if tile == start:
                    start= None
                    
                elif tile == end:
                    end= None
                
                tile.reset()
            if event.type == pygame.KEYDOWN:
                # Algorithm Call
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for tile in row:
                            tile.update_neighbors(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                # Hot Reset Grid
                if event.key == pygame.K_BACKSPACE and not started:
                    grid= make_grid(ROWS, width)
                    start= None
                    end= None
    pygame.quit()
    
main(WIN, WIDTH)

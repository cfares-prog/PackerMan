import pygame
import random

class TestGhost:
    
    def movement(self, game_map, packer, ghost):
        x, y= ghost.get_tile_position()
        dx, dy= ghost.DIRECTIONS[ghost.get_direction()]
        x+= dx
        y+= dy
        if game_map.is_wall(x, y):#if not wall keep moving if wall then change direction
            ghost.set_direction(random.choice(list(ghost.DIRECTIONS.keys())))
        
        ghost.step(game_map, packer)
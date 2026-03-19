from sprite_loader import SpriteSheet
import pygame

class PackerSprites:

    loader = SpriteSheet("temp.png");
    frames = [
            loader.get_sprite_scaled(1,1,1,1,1),
            loader.get_sprite_scaled(1,1,1,1,1),
            loader.get_sprite_scaled(1,1,1,1,1),
            loader.get_sprite_scaled(1,1,1,1,1)
    ]

    animations = {
            "right": frames,
            "left" : [pygame.transform.rotate(f, 180) for f in frames],
            "up" : [pygame.transform.rotate(f,90) for f in frames],
            "down" : [pygame.transform.rotate(f, 270) for f in frames],
    }


class Pacman:
    
    DIRECTIONS= {# x, y
        "down": (1, 0),
        "up":  (-1, 0),
        "right":(0, 1),
        "left": (0, -1),
    }
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.power = False
        self.direction = "right"
    
    def get_position(self):
        return {"row": self.x , "col": self.y}
    

    def set_power(self, status):
        self.power = status

    #def draw(self, win, gap):
    #    pygame.time.delay(5)
    #    pygame.display.update()

    def check_death(self, ghost_positions):
        if self.power:
            return False
        return (self.x, self.y) in ghost_positions

    def set_direction (self, name):
        self.direction_name = name
        self.direction = self.DIRECTIONS[name]

    def get_direction(self):
        return self.direction

    def step(self, map):
        dx, dy = self.direction
        self.x += dx
        self.y += dy

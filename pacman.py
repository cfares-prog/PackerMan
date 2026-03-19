from sprite_loader import SpriteSheet
import pygame

class PackerSprites:

    loader = SpriteSheet("temp.png");
    frame_1 = loader.get_sprite_scaled(1,1,1,1,1)
    frame_2 = loader.get_sprite_scaled(1,1,1,1,1)
    frame_3 = loader.get_sprite_scaled(1,1,1,1,1)
    frame_4 = loader.get_sprite_scaled(1,1,1,1,1)

class Pacman:
    # x:135 y;45
    
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
    
    def get_position(self):
        return {"row": self.x , "col": self.y}

    def set_power(self, status):
        self.power = status

    def draw(self, win, gap):
        win.blit(packer,(self.x* gap+ self.x,self.y* gap+ self.y))
        pygame.time.delay(5)
        pygame.display.update()
        
    def move_right(self):
        self.direction= self.DIRECTIONS["right"]
    def move_left(self):
        self.direction= self.DIRECTIONS["left"]
    def move_up(self):
        self.direction= self.DIRECTIONS["up"]
    def move_down(self):
        self.direction= self.DIRECTIONS["down"]

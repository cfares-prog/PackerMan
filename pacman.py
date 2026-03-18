from sprite_loader import SpriteSheet
import pygame

class pacman:
    spriteImage= SpriteSheet("sprites.png")
    packer= spriteImage.get_sprite_scaled(135, 45, 8, 8, 1.0)
    # x:135 y;45
    
    DIRECTIONS= {# x, y
        "down": (1, 0),
        "up": (-1, 0),
        "right":   (0, 1),
        "left": (0, -1),
    }
    
    def __init__(self, x, y, map, oX, oY):
        self.x= x
        self.y= y
        self.oX= oX
        self.oY= oY
        self.direction= self.DIRECTIONS["right"]
        self.map= map
    
    def draw(self, win, gap, map): 
        self.map= map
        win.blit(self.packer,(self.x* gap+ self.oX,self.y* gap+ self.oY))
        pygame.time.delay(5)
        pygame.display.update()
    
    def move(self):
        px= self.x + self.direction[0]
        py= self.y + self.direction[1]
        if not self.map.is_wall(px, py):
            self.map.eat_coin(px, py)
            x= px
            y= py
        
        
        
    def moveRight(self):
        self.direction= self.DIRECTIONS["right"]
    def moveLeft(self):
        self.direction= self.DIRECTIONS["left"]
        print("l")
    def moveUp(self):
        self.direction= self.DIRECTIONS["up"]
    def moveDown(self):
        self.direction= self.DIRECTIONS["down"]
from sprite_loader import SpriteSheet
from enum import Enum
import pygame

class States(Enum):
    CHASE = 1
    WITHDRAW = 2
    REVIVE = 3

class GhostSprites:
    TILE_WIDTH = 16
    SCALE = 1.5

    loader = SpriteSheet("sprites/ghostsSheet.png")
    
    revive_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 1,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 1,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 1,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 1,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 1,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 1,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 1,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 1,TILE_WIDTH, TILE_WIDTH, SCALE),
    }

    scaredy_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 3,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 3,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 3,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 3,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 3,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 3,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 3,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 3,TILE_WIDTH, TILE_WIDTH, SCALE),
    }

    red_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 4,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 4,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 4,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 4,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 4,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 4,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 4,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 4,TILE_WIDTH, TILE_WIDTH, SCALE),
    }

    pink_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 5,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 5,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 5,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 5,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 5,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 5,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 5,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 5,TILE_WIDTH, TILE_WIDTH, SCALE),
    }

    cyan_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 6,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 6,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 6,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 6,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 6,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 6,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 6,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 6,TILE_WIDTH, TILE_WIDTH, SCALE),
    }
    
    orange_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 7,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 7,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 7,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 7,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 7,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 7,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 7,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 7,TILE_WIDTH, TILE_WIDTH, SCALE),
    }
    
    yellow_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 8,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 8,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 8,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 8,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 8,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 8,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 8,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 8,TILE_WIDTH, TILE_WIDTH, SCALE),
    }
    
    green_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 9,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 9,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 9,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 9,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 9,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 9,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 9,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 9,TILE_WIDTH, TILE_WIDTH, SCALE),
    }
    
    crimson_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 10,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 10,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 10,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 10,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 10,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 10,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 10,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 10,TILE_WIDTH, TILE_WIDTH, SCALE),
    }
    
    purple_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 11,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 11,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 11,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 11,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 11,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 11,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 11,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 11,TILE_WIDTH, TILE_WIDTH, SCALE),
    }
    
    sky_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 12,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 12,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 12,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 12,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 12,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 12,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 12,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 12,TILE_WIDTH, TILE_WIDTH, SCALE),
    }
    
    blue_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 13,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 13,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 13,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 13,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 13,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 13,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 13,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 13,TILE_WIDTH, TILE_WIDTH, SCALE),
    }
    
    gold_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 14,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 14,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 14,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 14,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 14,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 14,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 14,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 14,TILE_WIDTH, TILE_WIDTH, SCALE),
    }
    
    forest_sprites = {
            "up"        : loader.get_sprite_scaled(TILE_WIDTH * 0,TILE_WIDTH * 15,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down"      : loader.get_sprite_scaled(TILE_WIDTH * 1,TILE_WIDTH * 15,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left"      : loader.get_sprite_scaled(TILE_WIDTH * 2,TILE_WIDTH * 15,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right"     : loader.get_sprite_scaled(TILE_WIDTH * 3,TILE_WIDTH * 15,TILE_WIDTH, TILE_WIDTH, SCALE),
            "upAlt"     : loader.get_sprite_scaled(TILE_WIDTH * 4,TILE_WIDTH * 15,TILE_WIDTH, TILE_WIDTH, SCALE),
            "downAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 5,TILE_WIDTH * 15,TILE_WIDTH, TILE_WIDTH, SCALE),
            "leftAlt"   : loader.get_sprite_scaled(TILE_WIDTH * 6,TILE_WIDTH * 15,TILE_WIDTH, TILE_WIDTH, SCALE),
            "rightAlt"  : loader.get_sprite_scaled(TILE_WIDTH * 7,TILE_WIDTH * 15,TILE_WIDTH, TILE_WIDTH, SCALE),
    }
    
class Ghost:

    DIRECTIONS = {
        "right": (1, 0),
        "left":  (-1, 0),
        "down":  (0, 1),
        "up":    (0, -1),
    }

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.frame_index = 0
        
        self.direction = "up"
        self.state = States.CHASE
        
        self.move_progress = 0
        self.speed = 0.1
        match color:
            case "revive"   : self.sprites = GhostSprites.revive_sprites
            case "scaredy"  : self.sprites = GhostSprites.scaredy_sprites
            
            case "red"      : self.sprites = GhostSprites.red_sprites
            case "pink"     : self.sprites = GhostSprites.pink_sprites
            case "cyan"     : self.sprites = GhostSprites.cyan_sprites
            case "orange"   : self.sprites = GhostSprites.orange_sprites
            
            case "yellow"   : self.sprites = GhostSprites.yellow_sprites
            case "green"    : self.sprites = GhostSprites.green_sprites 
            case "crimson"  : self.sprites = GhostSprites.crimson_sprites
            case "purple"   : self.sprites = GhostSprites.purple_sprites
            
            case "sky"      : self.sprites = GhostSprites.sky_sprites
            case "blue"     : self.sprites = GhostSprites.blue_sprites
            case "gold"     : self.sprites = GhostSprites.gold_sprites
            case "forest"   : self.sprites = GhostSprites.forest_sprites

    def set_direction(self, name):
        self.direction = name

    def get_direction(self):
        return self.direction

    def get_tile_position(self):
        return int(self.y), int(self.x)

    def step(self, game_map, pacman):
        dx, dy = self.DIRECTIONS[self.direction]
        target_x = self.x + dx
        target_y = self.y + dy

        if game_map.is_wall(target_y, target_x):
            self.move_progress = 0
            return

        self.move_progress += self.speed

        if self.move_progress >= 1:
            self.x = target_x
            self.y = target_y
            self.move_progress = 0

    def draw(self, win, tile_size, offset_x, offset_y):
        dx, dy = self.DIRECTIONS[self.direction]

        px = (self.x + dx * self.move_progress) * tile_size + offset_x
        py = (self.y + dy * self.move_progress) * tile_size + offset_y
        if self.state == States.WITHDRAW:
            active_sprites = GhostSprites.scaredy_sprites
        elif self.state == States.REVIVE:
            active_sprites = GhostSprites.revive_sprites
        else:
            active_sprites = self.sprites

        sprite = active_sprites[self.direction]

        win.blit(sprite, (px, py))

    def update_state(self,pacman):
        
        if pacman.power and self.state == States.CHASE:
            self.state = States.WITHDRAW
            self.speed = 0.05

        elif not pacman.power and self.state == States.WITHDRAW:
            self.state = States.CHASE
            self.speed = 0.1

    def check_collision(self, pacman):
        if (int(self.x), int(self.y)) == (int(pacman.x), int(pacman.y)):
            if self.state == States.WITHDRAW:
                self.state = States.REVIVE
                self.speed = 0.2 

            elif self.state == States.CHASE:
                return "GAME OVER"

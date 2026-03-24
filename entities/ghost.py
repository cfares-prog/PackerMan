from sprite_loader import SpriteSheet
from enum import Enum
import pygame

class States(Enum):
    CHASE = 1
    WITHDRAW = 2
    REVIVE = 3

class GhostSprites:
    TILE_WIDTH = 110
    SCALE = 0.2

    loader = SpriteSheet("ghosts.png")
    cyan_sprites = {
            "up": loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
    }

    pink_sprites = {
            "up": loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
    }

    orange_sprites = {
            "up": loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
    }

    red_sprites = {
            "up": loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
    }

    scaredy = {
            "up": loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
    }

    revive = {
            "up": loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "down":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "left":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
            "right":loader.get_sprite_scaled(0,0,TILE_WIDTH, TILE_WIDTH, SCALE),
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
        self.next_direction = "up"
        self.state = States.CHASE
        
        self.move_progress = 0
        self.speed = 0.1
        match color:
            case "orange": self.sprites = GhostSprites.orange_sprites
            case "cyan": self.sprites = GhostSprites.cyan_sprites
            case "pink": self.sprites = GhostSprites.pink_sprites
            case "red": self.sprites = GhostSprites.red_sprites

    def set_direction(self, name):
        self.direction = name

    def set_next_direction(self,name):
        self.next_direction = name

    def get_direction(self):
        return self.direction

    def get_tile_position(self):
        return int(self.y), int(self.x)

    def step(self, game_map, pacman):
        next_dx, next_dy = self.DIRECTIONS[self.next_direction]
        next_x = self.x + next_dx
        next_y = self.y + next_dy

        if not game_map.is_wall(next_y, next_x):
            self.direction = self.next_direction

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
            active_sprites = GhostSprites.scaredy
        elif self.state == States.REVIVE:
            active_sprites = GhostSprites.revive
        else:
            active_sprites = self.sprites

        sprite = active_sprites[self.direction]

        win.blit(sprite, (px, py))

    def update_state(self,pacman):
        
        if pacman.power and self.state == States.CHASE:
            self.state = States.WITHDRAW
            self.speed = 0.05

            opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
            self.set_next_direction(opposites[self.direction])

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

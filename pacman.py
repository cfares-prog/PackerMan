from sprite_loader import SpriteSheet
import pygame

class PackerSprites:
    TILE_WIDTH = 110
    SCALE = 0.2
    loader = SpriteSheet("sprites/packer_man.png")
    
    frames = [
        loader.get_sprite_scaled(0, 0, TILE_WIDTH, TILE_WIDTH, SCALE),
        loader.get_sprite_scaled(110, 0, TILE_WIDTH, TILE_WIDTH, SCALE),
        loader.get_sprite_scaled(220, 0, TILE_WIDTH, TILE_WIDTH, SCALE),
    ]

    animations = {
        "right": frames,
        "left" : [pygame.transform.rotate(f, 180) for f in frames],
        "up" : [pygame.transform.rotate(f, 90) for f in frames],
        "down" : [pygame.transform.rotate(f, 270) for f in frames],
    }

class Pacman:
    DIRECTIONS = {
        "right": (1, 0),
        "left":  (-1, 0),
        "down":  (0, 1),
        "up":    (0, -1),
    }
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.power = False
        self.direction = "right"
        self.next_direction = "right"
        
        self.move_progress = 0
        self.speed = 0.15
        self.frame_index = 0
    
    def get_position(self):
        return self.x, self.y
    
    def get_tile_position(self):
        return int(self.y), int(self.x)

    def set_next_direction(self, name):
        self.next_direction = name

    def set_power(self, status):
        self.power = status

    def draw(self, win, tile_size, offset_x, offset_y):
        dx, dy = self.DIRECTIONS[self.direction]

        px = (self.x + dx * self.move_progress) * tile_size + offset_x
        py = (self.y + dy * self.move_progress) * tile_size + offset_y

        frames = PackerSprites.animations[self.direction]
        self.frame_index += self.speed
        if self.frame_index >= len(frames):
            self.frame_index = 0

        frame = frames[int(self.frame_index)]
        win.blit(frame, (px, py))

    def check_death(self, ghost_positions):
        if self.power:
            return False
        return (self.x, self.y) in ghost_positions

    def set_direction(self, name):
        self.direction = name

    def get_direction(self):
        return self.direction

    def step(self, game_map):
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
            
            game_map.eat_coin(self.y, self.x)

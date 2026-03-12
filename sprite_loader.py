import pygame

class SpriteSheet:
    def __init__(self,filename):
        self.sheet = pygame.image.load(filename).convert_alpha()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        return sprite

    def get_sprite_by_grid(self, col, row, sprite_width, sprite_height):
        x = col * sprite_width
        y = row * sprite_height
        return self.get_sprite(x, y, sprite_width, sprite_height)

    def get_sprite_scaled(self, x, y, width, height, scale):
        sprite = self.get_sprite(x, y, width, height)
        new_size = (int(width*scale), int(height*scale))
        return pygame.transform.scale(sprite, new_size)

    def get_sprite_flipped(self, x, y, width, height, flip_x=False, flip_y=False):
        sprite = self.get_sprite(x, y, width, height)
        return pygame.transform.flip(sprite, flip_x, flip_y)

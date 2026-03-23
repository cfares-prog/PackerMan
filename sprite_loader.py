import pygame
import sys

WIN_SIZE = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (255, 0, 0)

class SpriteSheet:
    def __init__(self,filename):
        self.sheet = pygame.image.load(filename)

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

#temp not part of project, keep for later potential other projects
def run_inspector(file_path, tile_size=(9, 9)):
    pygame.init()
    
    ss = SpriteSheet(file_path)
    sheet_rect = ss.sheet.get_rect()
    
    screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE))
    pygame.display.set_caption("Spritesheet Coordinate Inspector")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 16)

    while True:
        screen.fill(BLACK) 
        screen.blit(ss.sheet, (0, 0))
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y < sheet_rect.height:
            grid_x = (mouse_x // tile_size[0]) * tile_size[0]
            grid_y = (mouse_y // tile_size[1]) * tile_size[1]
            col = mouse_x // tile_size[0]
            row = mouse_y // tile_size[1]

            pygame.draw.rect(screen, GRAY, (grid_x, grid_y, tile_size[0], tile_size[1]), 2)
            
            info_text = f"X: {mouse_x} Y: {mouse_y} | Snap X: {grid_x} Snap Y: {grid_y} | Col: {col} Row: {row}"

        else:
            info_text = "Move mouse over image to see coordinates"

        text_surf = font.render(info_text, True, WHITE)
        screen.blit(text_surf, (10, sheet_rect.height + 15))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_inspector("sprites/packer_man.png", tile_size=(110, 110))

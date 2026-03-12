import pygame
from sprite_loader import SpriteSheet  # your class

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# Load your sprite sheet
sheet = SpriteSheet("sprites.png")
# Or grid-based:
sprite = sheet.get_sprite_by_grid(0, 0, 8, 8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(sprite, (100, 100))  # draw sprite at (100,100)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


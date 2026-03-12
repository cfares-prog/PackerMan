import pygame
from map import tiles, WALL, PLAY, M_WIDTH, M_HEIGHT, TEMP_WIDTH, TILE_WIDTH, WIN
import random

class Ghost:

	def __init__(self, x, y, color):
		self.x = x  # row
		self.y = y  # column
		self.color = color

	def can_move(self, dx, dy):
		new_x = self.x + dx
		new_y = self.y + dy
		if 0 <= new_x < M_HEIGHT and 0 <= new_y < M_WIDTH:
			return tiles[new_x][new_y] != WALL
		return False

	def move_until_fail(self, direction):
		directions = {
			'left': (0, -1),
			'up': (-1, 0),
			'down': (1, 0),
			'right': (0, 1)
		}
		dx, dy = directions[direction]
		moved = False
		while self.can_move(dx, dy):
			self.x += dx
			self.y += dy
			moved = True
		return moved

	def draw(self, win, gap):
		pygame.draw.rect(win, PLAY, (self.y * gap, self.x * gap, TILE_WIDTH, TILE_WIDTH))


def find_ghost_start():
	for i, row in enumerate(tiles):
		for j, tile in enumerate(row):
			if tile == PLAY:
				return i, j
	return 1, 1             # IDK WHERE

def main():
	pygame.init()
	gap = TEMP_WIDTH // M_HEIGHT
	x, y = find_ghost_start()
	ghost = Ghost(x, y, "white")
	run = True
	direction = random.choice(['left', 'up', 'down', 'right'])
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		moved = ghost.move_until_fail(direction)
		if not moved:
			direction = random.choice(['left', 'up', 'down', 'right'])

		WIN.fill((0, 0, 0))
		for i, row in enumerate(tiles):
			for j, tile in enumerate(row):
				pygame.draw.rect(WIN, tile, (j * gap, i * gap, TILE_WIDTH, TILE_WIDTH))
		ghost.draw(WIN, gap)
		pygame.display.update()
	pygame.quit()
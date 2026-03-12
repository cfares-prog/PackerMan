import pygame
from map import tiles, WALL, PLAY, M_WIDTH, M_HEIGHT, TEMP_WIDTH, TILE_WIDTH, WIN

class Pacman:

	_directions = {		# MARK AS PRIV
			'left': (0, -1),
			'up': (-1, 0),
			'down': (1, 0),
			'right': (0, 1)
		}

	def __init__(self, x, y):
		self.x = x  # row
		self.y = y  # column

	def can_move(self, dx, dy):
		new_x = self.x + dx
		new_y = self.y + dy
		if 0 <= new_x < M_HEIGHT and 0 <= new_y < M_WIDTH:
			return tiles[new_x][new_y] != WALL
		return False

	def move_until_fail(self, direction):
		dx, dy = self._directions[direction]
		moved = False
		while self.can_move(dx, dy):
			self.x += dx
			self.y += dy
			moved = True
		return moved

	def draw(self, win, gap):
		pygame.draw.rect(win, PLAY, (self.y * gap, self.x * gap, TILE_WIDTH, TILE_WIDTH))

def find_pacman_start():
	for i, row in enumerate(tiles):
		for j, tile in enumerate(row):
			if tile == PLAY:
				return i, j
	return 1, 1

def main():
	pygame.init()
	gap = TEMP_WIDTH // M_HEIGHT
	x, y = find_pacman_start()
	pacman = Pacman(x,y)
	run = True
	direction = None
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					direction = 'up'
				elif event.key == pygame.K_DOWN:
					direction = 'down'
				elif event.key == pygame.K_LEFT:
					direction = 'left'
				elif event.key == pygame.K_RIGHT:
					direction = 'right'
		if direction:
			moved = pacman.move_until_fail(direction)
			if not moved:
				direction = None
		WIN.fill((0, 0, 0))
		for i, row in enumerate(tiles):
			for j, tile in enumerate(row):
				pygame.draw.rect(WIN, tile, (j * gap, i * gap, TILE_WIDTH, TILE_WIDTH))
		pacman.draw(WIN, gap)
		pygame.display.update()
	pygame.quit()
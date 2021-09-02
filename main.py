import pygame
import sys
# Import Cube Making Class so Code is clear
from asset import CreateAsset

pygame.init()
# Screen as tuple
screen_size = screen_width, screen_height = 508, 436
screen = pygame.display.set_mode(screen_size)
running = True
count = 0
# Make A Group so wouldn't make a list of variables for each cubes
cubes = pygame.sprite.Group()
# Cube Pos
pox = 5
poy = 5

# Row
for i in range(19):
	# Colums
  for i in range(14):
		cubex = CreateAsset(pox, poy, 30)
		pox += 36
		cubes.add(cubex)
		count += 1
	pox -= pox
	pox += 5
	poy += 3

while running:

	screen.fill(pygame.Color("Black"))
	cubes.draw(screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	pygame.display.flip()
pygame.quit()
sys.exit()

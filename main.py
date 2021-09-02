import pygame
import sys
# Import Cube Making Class so Code is clear
from asset import CreateAsset

# Size:
csize = 10

pygame.init()
# Screen as tuple
screen_size = screen_width, screen_height = 30*csize-20, 30*csize-20
screen = pygame.display.set_mode(screen_size)
running = True
count = 0
# Make A Group so wouldn't make a list of variables for each cubes
cubes = pygame.sprite.Group()
# Cube Pos
pox = 2
poy = 2

# Main Cube Creating:
for i in range(15):
	for i in range(14):
		cube = CreateAsset(pox, poy, 30)
		pox += 32
		cubes.add(cube)
	# Make the Pox 0, pox += 2 is the border 
	pox -= pox
	pox += 2
	# Cube Separation Under:
	poy += 32
	
# running = True
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
	
# If running is False: exit
pygame.quit()
sys.exit()

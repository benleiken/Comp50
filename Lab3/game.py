import pygame, os, sys
from pygame.locals import *
from random import randint
from Laser import *
from Enemy import *
from Battlecruiser import *

def load_image(image_name):
	''' The proper way to load an image '''
	try:
		image = pygame.image.load(image_name)
	except pygame.error, message:
		print "Cannot load image: " + image_name
		raise SystemExit, message
	return image.convert_alpha()
# Initialize all imported Pygame modules (a.k.a., get things started)
pygame.init()

# Set the display's dimensions
screenDimensions = (800, 600)
window = pygame.display.set_mode(screenDimensions, pygame.RESIZABLE)
pygame.display.set_caption('Battle for Ram Aras') # Set the window bar title

# Get the drawing surface and background
screen = pygame.display.get_surface() # This is where images are displayed
background = pygame.Surface(screen.get_size())

# Keep track of which arrow key was pressed
pressed = None

# Set up our two sprites: the caveman and the steak
if not pygame.font:
	print "Warning, fonts disabled"
if not pygame.mixer:
	print "Warning, sound disabled"

# Constants
FPS = 50
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
BC_IMAGE = 'battlecruiser.gif'
LASER_IMAGE = 'laser.gif'
LASER_SPEED = -10
COOLDOWN_TIME = 5
ENEMY_IMAGE = 'mutalisk.gif'
NUM_ENEMIES = 10
ENEMY_SPEED = -3


score = 0
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

gameover = False
	
	
bc = Battlecruiser(screen, BC_IMAGE, SCREEN_WIDTH/2, SCREEN_HEIGHT - 150, 0, 0)
lasers = []
enemy = Enemy(screen, ENEMY_IMAGE, randint(1,SCREEN_WIDTH), randint(1, SCREEN_HEIGHT), randint(-3,3), ENEMY_SPEED, 0)


bgimage = load_image("ram_aras.png") 
while gameover != True:
	time_passed = clock.tick(FPS)
        screen.fill(BACKGROUND_COLOR)
	screen.blit(bgimage, (0,0))
	score_display = font.render("Score: " + str(score), 1, (255, 255, 255))
	screen.blit(score_display, (10, 10))
	
	key = pygame.key.get_pressed()
	bc.dx = 0
	bc.dy = 0
	bc.draw()
	for laser in lasers:
		laser.update()
		laser.draw()
			
	if(enemy.active == False):
		enemy = Enemy(screen, ENEMY_IMAGE, randint(1,SCREEN_WIDTH), randint(1, SCREEN_HEIGHT/3), randint(-3,3), ENEMY_SPEED, 0)
	if(enemy.active == True):
		enemy.draw()
		enemy.update()
	pygame.display.flip()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()

	if key[pygame.K_UP]:
		pressed = "UP"
		bc.update(pressed)
	if key[pygame.K_DOWN]:
		pressed = "DOWN"
		bc.update(pressed)
	if key[pygame.K_LEFT]:
		pressed = "LEFT"
		bc.update(pressed)
	if key[pygame.K_RIGHT]:
		pressed = "RIGHT"
		bc.update(pressed)
	if key[pygame.K_SPACE]:
		if bc.ccounter == 0 :
			newLaser = Laser(screen, LASER_IMAGE, bc.x +48, bc.y, LASER_SPEED)
			newLaser.sound.play()
			lasers.append(newLaser)
			bc.ccounter = COOLDOWN_TIME
		else:
			bc.ccounter -= 1
	
	# Check for collisions
	for laser in lasers:
		if pygame.sprite.collide_rect(laser, enemy) and enemy.active == True:
			enemy.laser_collision()
			score = score + 100
	if pygame.sprite.collide_rect(bc, enemy) and enemy.active == True:
		bc.sound.play()
		gameover = True

while True:
	screen.fill(BACKGROUND_COLOR)
	score_display = font.render("GAME OVER!", 1, (255, 255, 255))
	screen.blit(score_display, (SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2))
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()


		


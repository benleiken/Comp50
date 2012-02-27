import pygame, os, sys
from pygame.locals import *
from random import randint
from Laser import *

class Battlecruiser(pygame.sprite.Sprite):
	'''A battlecruiser fires lasers'''
	
	def load_image(self, image_title):
		try:
			image = pygame.image.load(image_title)
		except pygame.error, message:
			print "Could not load image: " + image_title
			raise SystemExit, message
		return image.convert_alpha()
	
	def __init__(self, screen, img_name, x, y, dx, dy):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen

		self.image= self.load_image(img_name)
		self.rect = self.image.get_rect()

		self.image_w, self.image_h = self.image.get_size()
		self.x = x
		self.y = y

		self.dx = dx
		self.dy = dy
		
		self.ccounter = 0 #Time since last laser fired

	def draw(self):
		'''Draw the Battlecruiser'''
		draw_pos =  self.image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h /2)
		self.screen.blit(self.image, (self.x, self.y))

	def update(self, dir):
		'''Move the Battlecruiser, fire Lasers'''
		if dir == "UP":
			self.y = self.y - 3
		elif dir == "DOWN":
			self.y = self.y + 3
		elif dir == "LEFT":
			self.x = self.x - 3
		elif dir == "RIGHT":
			self.x = self.x + 3

if __name__ == "__main__":
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

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption('Battlecruiser')
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 28)
	
	
	bc = Battlecruiser(screen, BC_IMAGE, SCREEN_WIDTH/2, SCREEN_HEIGHT - 150, 0, 0)
	lasers = []
	while True:
		time_passed = clock.tick(FPS)
                
		screen.fill(BACKGROUND_COLOR)
		
		key = pygame.key.get_pressed()
		bc.dx = 0
		bc.dy = 0
		bc.draw()
		
		for laser in lasers:
			laser.update()
			laser.draw()
			

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
				lasers.append(Laser(screen, LASER_IMAGE, bc.x +48, bc.y, LASER_SPEED))
				bc.ccounter = COOLDOWN_TIME
			else:
			 	bc.ccounter -= 1

import pygame, os, sys
from pygame.locals import *
from random import randint

class Laser(pygame.sprite.Sprite):
	'''Lasers move from the bottom to the top of the screen'''
	
	def load_image(self, image_title):
		try:
			image = pygame.image.load(image_title)
		except pygame.error, message:
			print "Could not load image: " + image_title
			raise SystemExit, message
		return image.convert_alpha()
	
	def __init__(self, screen, img_name, x, y, dy):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen

		self.image= self.load_image(img_name)
		self.rect = self.image.get_rect()

		self.image_w, self.image_h = self.image.get_size()
		self.x = x
		self.y = y

		self.dx = 0
		self.dy = dy
		self.active = True

	def draw(self):
		'''Draw the Laser'''
		draw_pos =  self.image.get_rect().move(self.x - self.image_w / 2, self.y - self.image_h /2)
		self.screen.blit(self.image, (self.x, self.y))

	def update(self):
		'''Fire Lasers!'''
		self.y = self.y + self.dy

if __name__ == "__main__":
	if not pygame.font:
		print "Warning, fonts disabled"
	if not pygame.mixer:
		print "Warning, sound disabled"

	# Constants
	FPS = 50
	SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
	BACKGROUND_COLOR = (0, 0, 0)
	LASER_IMAGE = 'laser.gif'
	NUM_LASERS = 100
	LASER_SPEED = -10

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
	pygame.display.set_caption('Lasers!')
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 28)
	
	pressed = None
	
	lasers =[]

	while True:
		time_passed = clock.tick(FPS)

		screen.fill(BACKGROUND_COLOR)
		
		lasers.append(Laser(screen, LASER_IMAGE, randint(1,SCREEN_WIDTH), SCREEN_HEIGHT, LASER_SPEED))
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
					

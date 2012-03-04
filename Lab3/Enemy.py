import pygame, os, sys
from pygame.locals import *
from random import randint

class Enemy(pygame.sprite.Sprite):
	'''Enemies move around the screen -- can collide with the Battlecruiser or with Lasers'''
	
	def load_image(self, image_title):
		try:
			image = pygame.image.load(image_title)
		except pygame.error, message:
			print "Could not load image: " + image_title
			raise SystemExit, message
		return image.convert_alpha()
	
	def __init__(self, screen, img_name, x, y, dx, dy, thePlayer):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen

		self.image= self.load_image(img_name)
		self.rect = self.image.get_rect()

		self.image_w, self.image_h = self.image.get_size()
		self.x = x
		self.y = y

		self.dx = dx
		self.dy = dy
		self.rect.move(self.x, self.y)
		self.rect.topleft = (self.x, self.y)
		self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

		self.active = True
		self.thePlayer = thePlayer
	def laser_collision(self):
		self.image = self.load_image("laser_explosion.gif")
		self.active = False

	def draw(self):
		'''Draw the Enemy'''
		if(self.active == True):
			self.screen.blit(self.image, (self.x, self.y))

	def update(self):
		'''Move enemies'''
		if(self.active == True):
			if ((self.x + self.dx) <= 0):
				self.dx = self.dx * -1
			if ((self.x + self.dx) >= self.screen.get_size()[0]):
				self.dx = self.dx * -1
			if ((self.y + self.dy) <= 0):
				self.dy = self.dy * -1
			if ((self.y + self.dy) >= self.screen.get_size()[1]):
				self.dy = self.dy * -1

			self.y = self.y + self.dy
			self.x = self.x + self.dx
			self.rect.move(self.x, self.y)
			self.rect.topleft = (self.x, self.y)
			self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)


if __name__ == "__main__":
	if not pygame.font:
		print "Warning, fonts disabled"
	if not pygame.mixer:
		print "Warning, sound disabled"

	# Constants
	FPS = 50
	SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
	BACKGROUND_COLOR = (255, 255, 255)
	ENEMY_IMAGE = 'mutalisk.gif'
	NUM_ENEMIES = 10
	ENEMY_SPEED = -3

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
	pygame.display.set_caption('Enemies')
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 28)
	
	
	
	enemies =[]
	for i in range (NUM_ENEMIES):
		enemies.append(Enemy(screen, ENEMY_IMAGE, randint(1,SCREEN_WIDTH), randint(1, SCREEN_HEIGHT/2), randint(-3,3), ENEMY_SPEED, 0))

	while True:
		time_passed = clock.tick(FPS)

		screen.fill(BACKGROUND_COLOR)
		
		for enemy in enemies:
			enemy.update()
			enemy.draw()

		pygame.display.flip()
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
					


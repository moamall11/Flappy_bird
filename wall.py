import pygame
from pygame.sprite import Sprite
from random import choice
from random import randint

class Wall(Sprite):
	"""represent the walls"""
	def __init__(self,game):
		"""initialize the attributes of the walls"""
		super().__init__()
		self.settings=game.settings
		self.screen=game.screen
		self.screen_rect=self.screen.get_rect()

		self.width=20
		self.height=choice([200,250,280] \
			if game.settings.bird_speed >= 1.2 else [180,200])
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.bottom=self.screen_rect.bottom
		if randint(0,10)<5:
			self.rect.top=self.screen_rect.top
		self.rect.left=self.screen_rect.right
		self.walls_color=(50,50,50)
		if self.height>=250:
			self.walls_color=(250,0,0)
		self.x=float(self.rect.x)

	def update(self):
		"""update the position of the walls"""
		self.x-=self.settings.walls_speed
		self.rect.x=self.x

	def draw_wall(self):
		"""draw walls to the screen"""
		pygame.draw.rect(self.screen,self.walls_color,self.rect)

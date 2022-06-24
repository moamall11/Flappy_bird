import pygame

class Bird1:
	"""the bird"""
	def __init__(self,game):
		"""initialize the attributes of the bird"""
		self.settings=game.settings
		self.screen=game.screen
		self.screen_rect=self.screen.get_rect()
		self.image=pygame.image.load("images/bird.bmp")
		self.rect=self.image.get_rect()
		self.rect.midleft=self.screen_rect.midleft
		self.x=float(self.rect.x)
		self.y=float(self.rect.y)
		#movement flags.
		self.moving_right=False
		self.moving_left=False
		self.moving_up=False
		self.moving_down=True

	def draw_bird(self):
		"""draw the bird to the screen"""
		self.screen.blit(self.image,self.rect)

	def update(self):
		"""update the position of the bird"""
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.x+=self.settings.bird_speed
		if self.moving_left and self.rect.left>0:
			self.x-=self.settings.bird_speed
		self.rect.x=self.x
		if self.moving_up and self.rect.top>0:
			self.y-=self.settings.bird_speed
		if self.moving_down:
			self.y+=self.settings.bird_speed
		self.rect.y=self.y
import pygame
import json

class ScoreBoard:
	"""manage the score board"""
	def __init__(self,game):
		"""initialize the attributes of the score board"""
		self.settings=game.settings
		self.screen=game.screen
		self.screen_rect=self.screen.get_rect()
		self.width,self.height=1000,50
		self.rect=pygame.Rect(0,0,self.width,self.height)
		self.rect.top=self.screen_rect.top
		self.rect.centerx=self.screen_rect.centerx
		self.font=pygame.font.SysFont(None,48)
		self.text_color=(50,50,50)
		self.text_color2=(250,250,0)
		self.text_color3=(0,250,0)
		self.screen=game.screen
		self.screen_rect=self.screen.get_rect()
		self.high_score=self.get_high_score()
		self.prep_score()
		self.prep_birds()
		self.prep_high_score()

	def prep_birds(self):
		"""render the number of birds into an image"""
		birds_str=str(self.settings.birds)
		self.birds_img=self.font.render(
			birds_str,None,self.text_color2,self.settings.bg_color)
		self.birds_rect=self.birds_img.get_rect()
		self.birds_rect.left=self.rect.left

	def prep_score(self):
		"""render the score into an image"""
		score_str=str(self.settings.score)
		self.score_img=self.font.render(
			score_str,None,self.text_color,self.settings.bg_color)
		self.score_rect=self.score_img.get_rect()
		self.score_rect.center = self.rect.center

	def check_high_score(self):
		"""check for a new high score"""
		if self.settings.score > self.high_score:
			self.high_score=self.settings.score
			self.prep_high_score()

	def prep_high_score(self):
		"""render the high score into an image"""
		high_score_str=str(self.high_score)
		self.high_score_img=self.font.render(
			high_score_str,None,self.text_color3,self.settings.bg_color)
		self.high_score_rect=self.high_score_img.get_rect()
		self.high_score_rect.right=self.rect.right

	def get_high_score(self):
		"""return saved high score if it exists or return 0"""
		try:
			with open('high_score.json') as file:
				saved_high_score=json.load(file)
		except FileNotFoundError:
			return 0
		else:
			return saved_high_score


	def draw_score(self):
		"""draw the score to the screen"""
		self.screen.blit(self.score_img,self.score_rect)
		self.screen.blit(self.birds_img,self.birds_rect)
		self.screen.blit(self.high_score_img,self.high_score_rect)

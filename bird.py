import pygame
import sys
from random import random
from time import sleep
import json

from settings import Settings
from bird_object import Bird1
from wall import Wall
from score_board import ScoreBoard
from button import Button

class Bird:
	"""manage the game"""
	def __init__(self):
		"""initialize the attributes of the game"""
		pygame.init()
		self.settings=Settings()
		self.screen=pygame.display.set_mode(
			(self.settings.screen_width,self.settings.screen_height),pygame.RESIZABLE)
		pygame.display.set_caption("The Bird Game")
		self.bird=Bird1(self)
		self.walls=pygame.sprite.Group()
		self.sb=ScoreBoard(self)
		self.game_active=False
		self.play_button=Button(self,"Play")
		

	def run_game(self):
		"""the main loop of the game"""
		while True:
			self._check_events()
			if self.game_active:
				self.bird.update()
				self._create_walls()
				self.walls.update()
			self._update_screen()

	def _check_events(self):
		"""respond to the events from the player"""
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				self._close_game()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type==pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type==pygame.MOUSEBUTTONDOWN:
				mouse_pos=pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self,mouse_pos):
		"""respond when the player clicks Play"""
		button_clicked=self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.game_active:
			self._start_game()

	def _start_game(self):
		"""start the game"""
		self.game_active=True
		self.settings.initialize_dynamic_settings()
		self.sb.prep_score()
		self.sb.prep_birds()


	def _check_keydown_events(self,event):
		"""respond to keys pressed by the player"""
		if event.key==pygame.K_q:
			self._close_game()
		elif event.key==pygame.K_RIGHT:
			self.bird.moving_right=True
		elif event.key==pygame.K_LEFT:
			self.bird.moving_left=True
		elif event.key==pygame.K_UP:
			self.bird.moving_up=True
			self.bird.moving_down=False
		elif event.key==pygame.K_p:
			self._start_game()

	def _check_keyup_events(self,event):
		"""respond to keys released by the player"""
		if event.key==pygame.K_RIGHT:
			self.bird.moving_right=False
		elif event.key==pygame.K_LEFT:
			self.bird.moving_left=False
		elif event.key==pygame.K_UP:
			self.bird.moving_up=False
			self.bird.moving_down=True


	def _close_game(self):
		"""close the game"""
		saved_high_score=self.sb.get_high_score()
		if self.sb.high_score>saved_high_score:
			with open('high_score.json','w') as file:
				json.dump(self.sb.high_score,file)
		sys.exit()

	def _create_walls(self):
		"""create walls"""
		if random()<self.settings.walls_frequency:
			wall=Wall(self)
			self.walls.add(wall)
		for wall in self.walls.copy():
			if wall.rect.right<=0:
				self.walls.remove(wall)
				self.settings.score+=1
				self.sb.prep_score()
				self.sb.check_high_score()
				if self.settings.score%30==0:
					self.settings.speed_up()
					pygame.mixer.Sound("sounds/new_level.ogg").play()

		self._check_collisions()

	def _check_collisions(self):
		"""check for collisions"""
		collisions=pygame.sprite.spritecollideany(self.bird,self.walls)
		if collisions:
			self.walls.empty()
			self.bird.x=0
			self.bird.y=self.screen.get_rect().centery
			self.settings.birds-=1
			self.sb.prep_birds()
			sleep(0.5)
		if self.bird.rect.top>self.screen.get_rect().bottom:
			self.walls.empty()
			self.bird.x=0
			self.bird.y=self.screen.get_rect().centery
			self.settings.birds-=1
			self.sb.prep_birds()
			sleep(0.5)
		if self.settings.birds<=0:
			self.game_active=False


	def _update_screen(self):
		"""update the screen"""
		self.screen.fill(self.settings.bg_color)
		self.bird.draw_bird()
		for wall in self.walls.sprites():
			wall.draw_wall()
		self.sb.draw_score()
		if not self.game_active:
			self.play_button.draw_button()
		pygame.display.flip()


if __name__=='__main__':
	game=Bird()
	game.run_game()
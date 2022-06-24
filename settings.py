class Settings:
	"""settings for the bird game"""
	def __init__(self):
		"""initialize the attributes of the settings"""
		#screen settings.
		self.screen_width=1366
		self.screen_height=768
		self.bg_color=(230,230,230)
		#self.speed_scale=1.2
		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""initialize settings that change throughout the game"""
		self.score=0
		#walls settings.
		self.walls_speed=1
		self.walls_frequency=0.0073
		#bird settings.
		self.bird_speed=1
		self.birds=3


	def speed_up(self):
		"""speed up the game"""
		self.walls_speed+=0.2
		self.walls_frequency+=0.001
		self.bird_speed+=0.1
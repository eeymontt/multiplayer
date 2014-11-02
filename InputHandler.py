class InputHandler():
	def __init__(self):
		self.a = False
		self.d = False
		self.s = False
		self.w = False

	def update(self):
		key = pygame.key.get_pressed()
		self.w = key[pygame.K_w]
		self.s = key[pygame.K_s]
		self.a = key[pygame.K_a]
		self.d = key[pygame.K_d]
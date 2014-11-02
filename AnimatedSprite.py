class AnimatedSprite(pygame.sprite.Sprite):
	def __init__(self, images, fps=2):
		pygame.sprite.Sprite.__init__(self)
		self._images = images

		self._start = pygame.time.get_ticks()
		self._delay = 1000 / fps
		self._last_update = 0
		self._frame = 0

		# Call update to set our first image.
		self.update(pygame.time.get_ticks())

	def update(self, t):
		if t - self._last_update > self._delay:
			self._frame += 1
			self.image = self._images[self._frame]
			self._last_update = t

			return self._frame
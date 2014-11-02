class Entity():
	def __init__(self, level, x, y, ):
		self.level = level

	def render(self, screen):
		raise NotImplementedError, "Subclasses must define render()"
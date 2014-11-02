class Vector2():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	@staticmethod
	def add(vec1, vec2):
		return Vector2(vec1.x+vec2.x, vec1.y+vec2.y)

	@staticmethod
	def scale(vec, scalar):
		return Vector2(vec.x*scalar, vec1.y*scalar)
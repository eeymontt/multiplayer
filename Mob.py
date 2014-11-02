import Vector2

class Mob(Entity):
	def __init__(self, level, name, x, y, speed):
		Entity.__init__(level)
		self.name = name
		self.speed = speed

		self.position = Vector2(0,0)

		self.position.x = x
		self.position.y = y

		self.numSteps = 0
		self.isMoving = False
		self.movingDir = 1 #{0:UP, 1:DOWN, 2:LEFT, 3:RIGHT}
		self.scale = 1

	def move(self, xa, ya):
		if xa != 0 and ya != 0:
			move(xa, 0)
			move(ya, 0)
			self.numSteps -= 1
			return
		self.numSteps += 1
		if not self.hasCollided(xa, ya): #simplistic collision detection
			if ya < 0: self.movingDir = 0
			if ya > 0: self.movingDir = 1
			if xa < 0: self.movingDir = 2
			if xa > 0: self.movingDir = 3
			self.x += xa * self.speed
			self.y += ya * self.speed

	def hasCollided(self, xa, ya):
		raise NotImplementedError, "Subclasses must define hasCollided()"

	def getName(self): return self.name

	def getX(self): return self.position.x

	def getY(self): return self.position.y

	def getPosition(self): return self.position

	def setPosition(self, pos):
		self.position = pos
		return self.position

	def setX(self, x):
		self.position.x = xa
		return x

	def setY(self, y):
		self.position.y = y
		return y
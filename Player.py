import Mob

class Player(Mob):
	def __init__(self, level, name, x, y, input, collisionBox):
		Mob.__init__(level, "Player", x, y, 1)
		self.input = input
		self.collisionBox = CollisionBox(self.position.x, self.position.y, -16, 0, 32, 16)

		self.modifier = 8*self.scale
		self.xOffset = x - self.modifier/2
		self.yOffset = y - self.modifier/2

	def hasCollided(self, entity):
		return CollisionBox.isCollide(self.collisionBox, entity.collisionBox)

	def update(self):
		xa = 0
		ya = 0

		if input.up.isPressed(): ya -= 1
		if input.down.isPressed(): ya += 1
		if input.left.isPressed(): xa -= 1
		if input.right.isPressed(): xa += 1

		if xa != 0 or ya != 0:
			self.move(xa, ya)
			self.isMoving = True
		else:
			self.isMoving = False
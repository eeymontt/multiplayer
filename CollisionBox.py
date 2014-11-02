class CollisionBox():
	def __init__(self, x, y, xOffset, yOffset, width, height, solid=True): #x, y is top-left corner of box
		self.posX = x
		self.posY = y
		self.xOffset = xOffset #displacement from entity position
		self.yOffset = yOffset
		self.width = width
		self.height = height

		#self.upperY = y+height/2
		#self.lowerY = y-height/2
		#self.leftX  = x-width/2
		#self.rightX = x+width/2

		self.solid = solid #will it collide with other collision boxes?

	@staticmethod
	def isCollide(a,b):
		if a.solid and b.solid:
			return (abs(a.posX - b.posX)*2 < (a.width + b.width)) and (abs(a.posY - b.posY)*2 < (a.height + b.height))
		return False
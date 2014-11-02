import Player

class MPlayer(Player):
	def __init__(self, x, y, input, username, ipAddress, port):
		Player.__init__(x, y, input, username)
		self.ipAddress = ipAddress
		self.port = port
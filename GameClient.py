class GameClient():
	def __init__(self, game, ipAddress):
		self.game = game
		self.ipAddress = ipAddress
		
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		except socket.error, msg:
			print 'failed to create socket'
			print 'Error Code: ' + str(msg[0]) + ' Message ' + msg[1]

	def run(self):
		while True:
			try:
				packet, server = self.s.recvfrom(4096)
				print 'received "%s"' % data
			except socket.error, msg:
				print 'Error Code: ' + str(msg[0]) + ' Message ' + msg[1]

			print "Server >> "+str(packet.getData())

	def sendData(self, data):
		try:
			print 'sending "%s"' % message
			sent = self.s.sendto(self.message, self.server_address)
		except socket.error, msg:
				print 'Error Code: ' + str(msg[0]) + ' Message ' + msg[1]
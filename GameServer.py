import threading

class GameServer(threading.Thread):

	connectedPlayers = []

	def __init__(self, game, ipAddress):
		self.game = game
		self.ipAddress = ipAddress

		print 'starting up on %s port %s' % server_address

		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		except socket.error, msg:
			print 'failed to create socket'
			print 'Error Code: ' + str(msg[0]) + ' Message ' + msg[1]

		try:
			s.bind(server_address)
		except socket.error , msg:
			print 'bind failed'
			print 'Error Code: ' + str(msg[0]) + ' Message ' + msg[1]

	def run(self):
		while True:
			try:
				packet, address = self.s.recvfrom(4096)
				print 'received "%s"' % data
			except socket.error, msg:
				print 'Error Code: ' + str(msg[0]) + ' Message ' + msg[1]

			print "Client >> "+str(packet.getData())

	def sendData(self, data):
		try:
			print 'sending "%s"' % message
			sent = self.s.sendto(self.message, self.server_address)
		except socket.error, msg:
				print 'Error Code: ' + str(msg[0]) + ' Message ' + msg[1]

	def sendDataToAllClients(self, data): #byte_data
		for p in connectedPlayers:
			self.sendData(data, p.ipAddress, p.port)

	def parsePacket(data, address, port): #packet.getData(), packet.getAddress(), packet.getPort()
		message = data.trim()
		type = Packet.lookupPacket(message.substring(0,2))
		for case in Switch(type):
			if case("INVALID"):
				break

			if case("LOGIN"):
				packet = Packet00Login(data)
				print "["+address.getHostAddress()+":"+port+"] "+packet.getUsername()+" has connected."
				player = None
				if address.getHostAddress() == "localhost":
					player = MPlayer(100, 100, game.input, packet.getUsername(), address, port)
				else:
					player = MPlayer(100, 100, None, packet.getUsername(), address, port)
				
				if player != None:
					connectedPlayers.append(player)
					#add player to game

			if case("DISCONNECT"):
				break
			if case(): #default
				break
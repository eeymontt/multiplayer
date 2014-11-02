import Packet

class Packet00Login(Packet):
	def __init__(self, data):
		Packet.__init__("LOGIN")
		self.username = Packet.readData(data)

	def writeData(self, usr, client=False, server=False):
		if client:
			usr.sendData(self.getData())
		elif server:
			usr.sendDataToAllClients(self.getData())

	def getData(self):
		return "00" + self.username #where this whole thing is pickled

	def getUsername(self):
		return self.username
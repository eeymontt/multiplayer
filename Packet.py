class Packet():

	packetTypes = {-1:"INVALID", 00:"LOGIN", 01:"DISCONNECT"}

	def __init__(self, packetId):
		self.packetId = packetId

	def getId(self):
		return self.packetId

	def writeData(self, usr, client=False, server=False):
	 	raise NotImplementedError, "Subclasses must define writeData()"

	def readData(self, data): #not byte_data for now
		message = data.trim()
		return message.substring(2)

	def getData(self): #get the actual byte_array being sent
		raise NotImplementedError, "Subclasses must define getData()"
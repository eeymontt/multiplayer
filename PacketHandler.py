class PacketHandler():
	def pack(self, packet):
		p = pickle.dumps(packet, protocol=pickle.HIGHEST_PROTOCOL)
		return p

	def unpack(self, packet):
		p = pickle.loads(packet)
		return p

	@staticmethod
	def lookupPacket(id):
		for p in packetTypes:
			if p.getId() == id:
				return packetTypes[p]
		return packetTypes[-1]

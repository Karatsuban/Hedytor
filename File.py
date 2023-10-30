
class File:


	def __init__(self, filepath, lines, columns):
		self.filepath = filepath
		self.file = None
		self.lines = int(lines)
		self.columns = int(columns)
		print("HERE", lines, columns)
		self.bufferSize = self.lines*self.columns # number of character displayed
		self.bufferedHexContent = None # hexadecimal content
		self.bufferedANContent = None # alphanumerical represenntation
		self.currentFilePosition = None # file cursor

		self.open()


	def open(self):
		# open the file and populates the buffers
		self.file = open(self.filepath, "r+")
		self.bufferedHexContent = self.file.read(4*self.bufferSize)
		self.currentFilePosition = 4*self.bufferSize # get the offset


	def close(self):
		# close the file after use
		self.file.close()



	# Getters

	def getBuffers(self):
		return self.bufferedHexContent, self.bufferedANContent

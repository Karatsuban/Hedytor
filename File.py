
class File:


	def __init__(self, filepath, lines, columns):
		self.filepath = filepath
		self.file = None
		self.lines = int(lines)
		self.columns = int(columns)
		print("HERE", lines, columns)
		self.bufferSize = self.lines*self.columns # number of character displayed
		self.bufferedContent = None # buffered file content
		self.bufferedHex = None # hexadecimal content
		self.bufferedAN = None # alphanumerical represenntation
		self.currentFilePosition = None # file cursor

		self.open()


	def open(self):
		# open the file and populates the buffers
		self.file = open(self.filepath, "rb+")
		self.bufferedContent = self.file.read(4*self.bufferSize).hex()
		self.currentFilePosition = 4*self.bufferSize # get the offset
		self.setBuffs()

	def setBuffs(self):
		temp = [self.bufferedContent[k:k+2] for k in range(0, len(self.bufferedContent), 2)]
		print("temp = ", temp)
		self.bufferedHex = " ".join(temp)
		self.bufferedAN = ""
		for k in temp:
			try:
				char = bytes.fromhex(k).decode()
			except UnicodeDecodeError:
				char = "."
			except ValueError:
				print("Cant decode "+k)
			print(k, end=" ")
			self.bufferedAN += char
		print()
		#self.bufferedANContent = "".join([bytes.fromhex(k) for k in self.bufferedHexContent])

	def close(self):
		# close the file after use
		self.file.close()



	# Getters

	def getBuffers(self):
		return self.bufferedHex, self.bufferedAN

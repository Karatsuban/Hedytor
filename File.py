
class File:


	def __init__(self, filepath ):
		self.filepath = filepath
		self.file = None
		self.content = [] # file content


	def open(self):
		# open the file and populates the buffers
		try :
			self.file = open(self.filepath, "rb+")
		except OSError:
			return -1
		else:
			line = self.file.readline().hex()
			while line != "":
				self.content += [line[k:k+2] for k in range(0, len(line), 2)]
				line = self.file.readline().hex()


	def close(self):
		# close the file after use
		self.file.close()



	# Getters

	def getContent(self):
		return self.content

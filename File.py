import mimetypes
import PIL.Image

class File:


	def __init__(self, filepath=None ):
		self.filepath = filepath
		self.file = None
		self.content = [] # file content
		self.isPicture = False
		self.hasExif = False
		self.exifData = None

		# Guess the file's type and act accordingly
		self.guessType()


	def open(self):
		# open the file and populates the buffers
		if self.filepath is None:
			# BLANK FILE OPENED
			greeting = "This is a blank document".encode().hex()
			self.content = [greeting[k:k+2] for k in range(0, len(greeting), 2)]
			return

		try :
			self.file = open(self.filepath, "rb+")
		except OSError:
			return -1
		else:
			line = None 
			while line != "":
				line = self.file.readline().hex()
				self.content += [line[k:k+2] for k in range(0, len(line), 2)]


	def guessType(self):
		if self.filepath is None:
			return

		my_type = mimetypes.guess_type(self.filepath)
		if (my_type[0] is not None):
			if (my_type[0].split('/')[0] == 'image'):
				self.isPicture = True
				self.storeExifData()
	

	def storeExifData(self):
		img = PIL.Image.open(self.filepath)
		raw_exif = img.getexif()
		items = raw_exif.items()
		if len(items) == 0:
			self.hasExif = False
			self.exifData = None
		else:
			self.hasExif = True
			self.exifData = dict()
			for key, val in items:
				self.exifData[key] = str(val)
		img.close()


	def close(self):
		# close the file after use
		if self.filepath is not None:
			self.file.close()


	def saveTo(self, filename, content):
		# save the content to file
		with open(filename, "wb") as file:
			for a in range(0, len(content), 4096):
				file.write(bytes.fromhex("".join(content[a:a+4096])))

	# Getters

	def getContent(self):
		return self.content

	def getExifData(self):
		return self.exifData

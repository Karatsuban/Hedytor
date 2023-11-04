import mimetypes
import PIL.Image

class File:


	def __init__(self, filepath ):
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
		try :
			self.file = open(self.filepath, "rb+")
		except OSError:
			return -1
		else:
			line = self.file.readline().hex()
			while line != "":
				self.content += [line[k:k+2] for k in range(0, len(line), 2)]
				line = self.file.readline().hex()


	def guessType(self):
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
			print(self.exifData)
		img.close()


	def close(self):
		# close the file after use
		self.file.close()



	# Getters

	def getContent(self):
		return self.content

	def getExifData(self):
		print("getExifData called !")
		return self.exifData

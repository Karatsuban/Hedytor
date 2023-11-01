from PySide6.QtCore import *
import math

class StringModel(QAbstractTableModel):

	def __init__(self, data, hexType = True, parent = None):
		super().__init__(parent)
		self.characters = data
		self.hexType = hexType
		print("len = ", len(self.characters))



	def columnCount(self, parent = None):
		#print("My size is : "+self.size())
		return 16
	

	def rowCount(self, parent = None):
		return math.ceil(len(self.characters)/self.columnCount())
	
	
	def data(self, index, role = Qt.DisplayRole):
		if role == Qt.DisplayRole:
			row = index.row()
			column = index.column()
			offset = self.columnCount()*row+column
			if offset > len(self.characters)-1:
				return None
			else:
				retChar = self.characters[offset]
				if self.hexType:
					return retChar
				else:
					if int(retChar, 16) <= 31:
						retChar = "."
					else:
						retChar = bytes.fromhex(retChar).decode()
					return retChar
		return None


	def headerData(self, section, orientation, role):
		if role == Qt.DisplayRole:
			if orientation == Qt.Horizontal:
				if self.hexType:
					return self.toHexRepr(section, 2)
				else:
					return
			elif orientation == Qt.Vertical:
				return self.toHexRepr(section, 5)
	
	def toHexRepr(self, val, nb_zeroes):
		return format(val, "0"+str(nb_zeroes)+"x")

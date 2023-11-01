from PySide6.QtCore import *
import math

class StringModel(QAbstractTableModel):

	def __init__(self, data, hexType = True, parent = None):
		super().__init__(parent)
		self.characters = data


	# reimplementations

	def columnCount(self, parent = None):
		return 16
	

	def rowCount(self, parent = None):
		return math.ceil(len(self.characters)/self.columnCount())
	
	
	def data(self, index, role = Qt.DisplayRole):
		if role == Qt.DisplayRole:
			offset = self.indexToOffset(index)
			if offset > len(self.characters)-1:
				return None
			else:
				return self.characters[offset]
		return None


	def headerData(self, section, orientation, role):
		if role == Qt.DisplayRole:
			if orientation == Qt.Horizontal:
				return self.toHexRepr(section, 2)
			elif orientation == Qt.Vertical:
				return self.toHexRepr(section, 5)

	
	def setData(self, index, value, role = Qt.EditRole):
		# returns True if successful operation
		offset = self.indexToOffset(index)
		self.characters[offset] = value
		return True
	

	def flags(self, index):
		if self.indexToOffset(index) >= len(self.characters):
			return Qt.NoItemFlags
		return Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsEnabled|Qt.ItemNeverHasChildren;


	# signals

	def dataChanged(self, topLeft, bottomRight):
		pass
		


	# helper function

	def indexToOffset(self, index):
		return self.columnCount()*index.row()+index.column()

	def toHexRepr(self, val, nb_zeroes):
		return format(val, "0"+str(nb_zeroes)+"X")

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
		isError = False;
		for s in value:
			if not s.isdigit():
				isError = True

		if not isError:
			offset = self.indexToOffset(index)
			self.characters[offset] = value
		return isError


	def insertData(self, index, value, role = Qt.EditRole):
		# insert NEW value at the index


		if len(value) == 1:
			self.setData(index, value[0], role)
			return

		offset = self.indexToOffset(index)
		self.characters.pop(offset)

		total_inserted = (index.column()+len(value)-1)//16
		current_row = index.row()
		isAddingRow = False

		if (total_inserted != 0):
			isAddingRow = True
			parent = self.offsetToIndex(len(self.characters)-1)
			self.beginInsertRows(parent, self.rowCount(), self.rowCount()+total_inserted)

		for val in value:
			self.characters.insert(offset, val)
		
		if isAddingRow:
			self.endInsertRows()


	def deleteDataAt(self, index):
		# delete the data at the given index
		offset = self.indexToOffset(index)

		if offset < 0 or offset >= len(self.characters):
			return

		isRemovingRow = False

		if len(self.characters)%self.columnCount() == 15:
			isRemovingRow = True
			parent = self.offsetToIndex(len(self.characters)-1)
			self.beginRemoveRows(parent, self.rowCount(), self.rowCount()-1)

		self.characters.pop(offset)

		if isRemovingRow:
			self.endRemoveRows()


	def flags(self, index):
		if self.indexToOffset(index) >= len(self.characters):
			return Qt.NoItemFlags
		return Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsEnabled|Qt.ItemNeverHasChildren;


	# signals

	def dataChanged(self, topLeft, bottomRight):
		pass
		

	# GETTERS

	def getData(self):
		return self.characters


	# helper function

	def indexToOffset(self, index):
		return self.columnCount()*index.row()+index.column()

	def offsetToIndex(self, offset):
		row = offset//self.columnCount() 
		col = offset%self.columnCount()
		return self.index(row, col)

	def toHexRepr(self, val, nb_zeroes):
		return format(val, "0"+str(nb_zeroes)+"X")

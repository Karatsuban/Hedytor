from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import string

class HexDelegate(QStyledItemDelegate):


	def __init__(self, parent = None):
		super().__init__(parent)
		self.parent = parent
	


	def displayText(self, value, locale):
		return value

	def createEditor(self, parent, option, index):
		editor = QLineEdit(parent)
		return editor


	def setEditorData(self, editor, index):
		# create the editor and set its value
		value = index.data(Qt.DisplayRole)
		editor.setText(value)


	def setModelData(self, editor, model, index):
		# get the new value from the editor and call the model to set it
		valueFromEditor = editor.text()


		for char in valueFromEditor:
			if (char not in "0123456789ABCDEabcdef"):
				return

		valuesToInsert = []
		for count in range(0, len(valueFromEditor), 2):
			val = valueFromEditor[count:count+2]
			if len(val) == 1:
				val = "0"+val
			valuesToInsert.append(val)

		model.insertData(index, valuesToInsert[::-1])

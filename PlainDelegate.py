from PySide6.QtWidgets import *
from PySide6.QtCore import *

class PlainDelegate(QStyledItemDelegate):

	def __init__(self, model, parent = None):
		super().__init__(parent)
		self.model = model
		self.parent = parent
	
	def displayText(self, value, locale):
		if int(value, 16) <= 31:
			return "."
		return bytes.fromhex(value).decode()


	def createEditor(self, parent, option, index):
		editor = QLineEdit(parent)
		editor.setMaxLength(2) # only 2 characters
		return editor


	def setEditorData(self, editor, index):
		value = index.data(Qt.DisplayRole)


	def setModelData(self, editor, model, index):
		value = bytes(editor.text(), 'utf-8').hex()
		model.setData(index, value)

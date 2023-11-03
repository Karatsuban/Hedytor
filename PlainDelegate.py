from PySide6.QtWidgets import *
from PySide6.QtCore import *
import string

class PlainDelegate(QStyledItemDelegate):

	# all the printable chars, text and indices
	printable_chars = string.ascii_letters + string.digits + string.punctuation + ' '
	pr_id = [ord(k) for k in printable_chars]

	def __init__(self, model, parent = None):
		super().__init__(parent)
		self.model = model
		self.parent = parent
	
	def displayText(self, value, locale):
		if int(value, 16) not in self.pr_id:
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

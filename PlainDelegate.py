from PySide6.QtWidgets import *
from PySide6.QtCore import *
import string

class PlainDelegate(QStyledItemDelegate):

	# all the printable chars, text and indices
	printable_chars = string.ascii_letters + string.digits + string.punctuation + ' '
	pr_id = [ord(k) for k in printable_chars]


	def __init__(self, parent = None):
		super().__init__(parent)
		self.parent = parent


	def getRepr(self, value):
		if int(value, 16) not in self.pr_id:
			return "."
		return bytes.fromhex(value).decode()


	def displayText(self, value, locale):
		return self.getRepr(value)

	def createEditor(self, parent, option, index):
		editor = QLineEdit(parent)
		return editor


	def setEditorData(self, editor, index):
		# create the editor and set its value
		value = index.data(Qt.DisplayRole)
		editor.setText(self.getRepr(value))


	def setModelData(self, editor, model, index):
		# get the new value from the editor and call the model to set it
		valueFromEditor = editor.text()

		valuesToInsert = "".join(valueFromEditor[::-1].encode().hex())
		valuesToInsert = [valuesToInsert[k:k+2] for k in range(0, len(valuesToInsert), 2)]
		model.insertData(index, valuesToInsert)

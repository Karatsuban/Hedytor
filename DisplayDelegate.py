from PySide6.QtWidgets import *

class DisplayDelegate(QStyledItemDelegate):

	def __init__(self, model, parent = None):
		super().__init__(parent)
		self.model = model
		self.parent = parent
	
	def displayText(self, value, locale):
		if int(value, 16) <= 31:
			return "."
		return bytes.fromhex(value).decode()

	"""
	def setEditorData():
		pass
	"""

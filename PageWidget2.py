from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import EditorLayout
import StringModel
import File
import DisplayDelegate

class PageWidget2(QWidget):

	def __init__(self, filename):
		super().__init__()
		self.filename = filename
		self.file = File.File(self.filename)
		self.file.open() # read the file content

		self.model = StringModel.StringModel(self.file.getContent())
		#self.modelHex = StringModel.StringModel(self.file.getContent())
		#self.modelPlain = StringModel.StringModel(self.file.getContent(), False)

		self.font = QFont("Monospace")
		self.layout = QHBoxLayout()#working
		self.setLayout(self.layout)
		self.hexEditor = QTableView()
		self.plainEditor = QTableView()
		
		self.hexEditor.setFont(self.font)
		self.hexEditor.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
		self.hexEditor.setModel(self.model)
		self.hexEditor.show()
		self.hexEditor.setGridStyle(Qt.NoPen)
		self.hexEditor.resizeColumnsToContents()
		self.hexEditor.resizeRowsToContents()

		#self.plainEditor.setWordWrapMode(QTextOption.WrapAnywhere) # don't cut any word

		self.delegate = DisplayDelegate.DisplayDelegate(self.plainEditor)
		self.plainEditor.setItemDelegate(self.delegate)
		self.plainEditor.setFont(self.font)
		self.plainEditor.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
		self.plainEditor.setModel(self.model)
		self.plainEditor.show()
		self.plainEditor.setGridStyle(Qt.NoPen)
		self.plainEditor.resizeColumnsToContents()
		self.plainEditor.resizeRowsToContents()

		self.plainEditor.setSelectionModel(self.hexEditor.selectionModel())

		# adding the widgets to the layout
		self.layout.addWidget(self.hexEditor)#working
		self.layout.addWidget(self.plainEditor)#working

	
		#self.resizeEditors()

	


	def resizeEditors(self):
		size = self.size()
		self.hexEditor.resize()
		self.plainEditor.resize()


	def setText(self, text):
		self.model.setStringlist(text)

	def setHexText(self, text):
		#self.hexEditor.setText(text)
		pass
	

	def setPlainText(self, text):
		#self.plainEditor.setText(text)
		pass

	def close(self):
		self.file.close() # close the file
		self.hexEditor.close()
		self.plainEditor.close()
	
	"""	
	def resizeEvent(self, event):
		self.resizeEditors()
	"""

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import StringModel
import File
from PlainDelegate import *

class PageWidget(QWidget):

	def __init__(self, filename):
		super().__init__()
		self.filename = filename
		self.file = File.File(self.filename)
		self.file.open() # read the file content

		# initiate only one model
		self.model = StringModel.StringModel(self.file.getContent())

		self.font = QFont("Monospace")
		self.layout = QHBoxLayout()
		self.setLayout(self.layout)

		# create two different views
		self.hexEditor = QTableView()
		self.plainEditor = QTableView()


		# set the hex editor's values
		self.hexEditor.setFont(self.font)
		self.hexEditor.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
		self.hexEditor.setModel(self.model)
		self.hexEditor.setGridStyle(Qt.NoPen)
		self.hexEditor.resizeColumnsToContents()
		self.hexEditor.resizeRowsToContents()


		# set the plain editor's values
		self.delegate = PlainDelegate(self.plainEditor)
		self.plainEditor.setItemDelegate(self.delegate)
		self.plainEditor.setFont(self.font)
		self.plainEditor.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
		self.plainEditor.setModel(self.model)
		self.plainEditor.setGridStyle(Qt.NoPen)
		self.plainEditor.resizeColumnsToContents()
		self.plainEditor.resizeRowsToContents()
		self.plainEditor.setShowGrid(False) # hide the grid
		#self.plainEditor.horizontalHeader().hide() # hide the horizontal header

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

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import StringModel
import File
from PlainDelegate import *
from ExportWindow import *

class PageWidget(QWidget):

	def __init__(self, filename):
		super().__init__()
		self.filename = filename
		self.file = File.File(self.filename)
		self.file.open() # read the file content

		# initiate only one model
		self.model = StringModel.StringModel(self.file.getContent())

		# define font and layout
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


		# synchronize the selection across the two views
		self.plainEditor.setSelectionModel(self.hexEditor.selectionModel())

		print(self.hexEditor.verticalScrollBar())
		self.plainEditor.setVerticalScrollBar(self.hexEditor.verticalScrollBar())
		self.scrollBar = self.plainEditor.verticalScrollBar()

		# adding the widgets to the layout
		self.layout.addWidget(self.hexEditor)
		self.layout.addWidget(self.scrollBar)
		self.layout.addWidget(self.plainEditor)




		# spawn a new window if the file opened is an image
		if self.file.isPicture:
			if self.file.hasExif:
				self.exportWindow = ExportWindow(self.file.getExifData())
				self.exportWindow.show()
		
	


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

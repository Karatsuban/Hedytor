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
		self.isShowingExport = False # whether the exportWindow is open

		# initiate only one model
		self.model = StringModel.StringModel(self.file.getContent())

		# define font and layout
		self.font = QFont("Monospace")
		self.layout = QGridLayout()
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

		self.plainEditor.setVerticalScrollBar(self.hexEditor.verticalScrollBar())
		self.plainEditor.setHorizontalScrollBar(self.hexEditor.horizontalScrollBar())
		self.vScrollBar = self.plainEditor.verticalScrollBar()
		self.hScrollBar = self.plainEditor.horizontalScrollBar()

		# adding the widgets to the layout
		self.layout.addWidget(self.hexEditor, 0, 0)
		self.layout.addWidget(self.vScrollBar, 0, 1)
		self.layout.addWidget(self.plainEditor, 0, 2)
		self.layout.addWidget(self.hScrollBar, 1, 0, 1, 3)


		
		self.exportExif()
		
	
	def exportExif(self):
		# spawn a new window if the file opened is an image
		if self.file.isPicture:
			if self.file.hasExif:
				self.exportWindow = ExportWindow(self.file.getExifData())
				self.exportWindow.show()
				self.isShowingExport = True


	def resizeEditors(self):
		size = self.size()
		self.hexEditor.resize()
		self.plainEditor.resize()


	def close(self):
		self.file.close() # close the file
		self.hexEditor.close()
		self.plainEditor.close()

		# close the export window if it exists
		if self.isShowingExport:
			self.exportWindow.close()
	
	"""	
	def resizeEvent(self, event):
		self.resizeEditors()
	"""

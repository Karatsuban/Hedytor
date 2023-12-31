import random
import sys
import os
import time
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtNetwork import *

import File
import PageWidget

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setMinimumSize(600,500)

		self.font = QFont("Monospace")

		# central widget
		central_widget = QWidget(self)
		self.setCentralWidget(central_widget)

		# create layout
		layout = QVBoxLayout()
		central_widget.setLayout(layout)

		# set status bar
		self.setStatusBar(QStatusBar(self))
		self.status = self.statusBar()
		self.status.addPermanentWidget(QLabel("Hedytor v1.0"))

		# creat network manager
		self.network_manager = QNetworkAccessManager()
		self.network_manager.finished.connect(self.handle_response)


		# Add a menubar
		self.menu = self.menuBar()


		# Action buttons
	
		openButton = QAction("&Open file", self)
		openButton.triggered.connect(self.openFrom)
		saveButton = QAction("&Save file", self)
		saveButton.triggered.connect(self.saveTo)
		exportJSONButton = QAction("&Export to JSON", self)
		exportJSONButton.triggered.connect(self.exportToJSON)
		newFileButton = QAction("&New file", self)
		newFileButton.triggered.connect(self.openBlank)


		# add menues
		self.file_menu = self.menu.addMenu("&File")

		# Add actions to menues
		self.file_menu.addAction(openButton)
		self.file_menu.addAction(newFileButton)
		self.file_menu.addAction(saveButton)
		self.file_menu.addAction(exportJSONButton)


		# Add widgets

		self.filePathLineEdit = QLineEdit()
		self.filePathLineEdit.setPlaceholderText("Enter a file path")

		# creating "open file" button and its logic
		self.openFileButton = QPushButton("Open file")
		self.openFileButton.clicked.connect(self.openFileFromButton)
		
		self.networkFileCheckBox = QCheckBox("Network file")

		
		# Add widgets to layout

		firstRowLayout = QHBoxLayout()
		layout.addLayout(firstRowLayout)
		
		secondRowLayout = QHBoxLayout()
		layout.addLayout(secondRowLayout)
		
		firstRowLayout.addWidget(self.filePathLineEdit)
		firstRowLayout.addWidget(self.openFileButton)
		firstRowLayout.addWidget(self.networkFileCheckBox)

		# create tab widget and set its attributes
		self.tab = QTabWidget(self)
		self.tab.setMovable(True)
		self.tab.setTabsClosable(True)
		layout.addWidget(self.tab)

		# set action when closing the tab index
		self.tab.tabCloseRequested.connect(lambda index: self.removeTab(index))

		self.blankNb = 0 # number of blank files opened
		



	def closeEvent(self, event):
		# handle the close event by closing each thing correcly 
		while (self.tab.count() != 0):
			self.removeTab(0)
		event.accept() # accept the close event


	def switchToTab(self, index):
		# switch to the given tab
		self.tab.setCurrentIndex(index)

	def openBlank(self):
		# open a blank file
		self.openFile(None)


	def openFileFromButton(self):
		# opening a file from a button press

		filepath = self.filePathLineEdit.text()
		if len(filepath) == 0:
			return

		# open either a local or remote file
		if (self.networkFileCheckBox.isChecked()):
			self.send_request(filepath)
		else:
			self.openFile(filepath)


	def openFile(self, filepath=None):
		# open a file if it exists
		
		if filepath is None:
			# open a blank file
			page = PageWidget.PageWidget(None)
			self.addTab(page, "File_{}".format(self.blankNb))
			self.blankNb += 1
			return

		if (os.path.isfile(filepath)):
			# opening the file and creating a new page
			page = PageWidget.PageWidget(filepath)
			filename = os.path.split(filepath)[-1]
			self.addTab(page, filename)
			self.filePathLineEdit.clear()
		else:
			# could not open
			self.status.showMessage("File not found: '"+str(filepath)+"'", 3000)
			self.filePathLineEdit.setFocus() # set the focus back to the line edit


	def addTab(self, page, title):
		# add page to tab, with title as a title
		self.tab.addTab(page, title)
		index = self.tab.count()-1
		self.switchToTab(index)


	def removeTab(self, index):
		# remove the page at index
		page = self.tab.widget(index)
		self.tab.removeTab(index)
		page.close()


	def	openFrom(self):
		# open a file from a file dialog
		dialog = QFileDialog(self)
		dialog.setFileMode(QFileDialog.AnyFile)
		dialog.setViewMode(QFileDialog.Detail)
		if dialog.exec():
			filenames = dialog.selectedFiles()
		else:
			filenames = []
		for filename in filenames:
			self.openFile(filename)


	def saveTo(self):
		# save the the current file, with a file manager
		current_widget = self.tab.currentWidget() # get current widget
		if current_widget is not None:
			filepath = current_widget.file.filepath
			dialog = QFileDialog(self)
			dialog.AcceptMode(QFileDialog.AcceptSave)
			dialog.setFileMode(QFileDialog.AnyFile)
			dialog.setViewMode(QFileDialog.Detail)

			if dialog.exec():
				filename = dialog.selectedFiles()
				current_widget.saveTo(filename[0])

			

	def exportToJSON(self):
		# export the current file's data to JSON if possible
		current_widget = self.tab.currentWidget()
		if current_widget is not None:
			ret = current_widget.exportExif()
			if ret is not None:
				self.status.showMessage(ret, 3000)



	def send_request(self, url):
		# request a url
		if url:
			self.openFileButton.setEnabled(False) # disable the button
			self.start_time = time.time()
			request = QNetworkRequest(QUrl(url))
			self.network_manager.get(request)


	def handle_response(self, reply):
		# handle the response by saving the file
		elapsed_time = time.time() - self.start_time
		self.openFileButton.setEnabled(True) # enable the button
		self.status.showMessage(f"Response time : {elapsed_time:.2f} seconds", 3000)
		if reply.error() == QNetworkReply.NoError:
			status_code = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
			
			# creating a temp file with a random name to avoid overwriting another
			outputFileName = "tmp/file_"+str(random.random()).split(".")[1]
			self.createTempDir()

			# trasnferring the content into a file
			with open(outputFileName, "w") as file:
				lines = reply.readAll().data().decode("utf-8")
				file.write(lines)
			
			self.networkFileCheckBox.setCheckState(Qt.Unchecked)
			self.openFile(outputFileName) # finally open the downloaded file
			self.status.showMessage("File successfully downloaded at '"+outputFileName+"'", 3000)
		else:
			# could not get the file
			self.status.showMessage("Error: "+reply.errorString(), 3000)
			self.filePathLineEdit.setFocus() # set the focus back to the line edit


	def createTempDir(self):
		# create the /tmp dir if does not exist
		if (not os.path.exists("tmp/")):
			os.makedirs("tmp/")


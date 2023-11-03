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

		# File list
		self.fileList = []


		# central widget
		central_widget = QWidget(self)
		self.setCentralWidget(central_widget)

		layout = QVBoxLayout()
		central_widget.setLayout(layout)

		self.setStatusBar(QStatusBar(self))
		self.status = self.statusBar()
		self.status.addPermanentWidget(QLabel("Hedytor v1.0"))

		#self.network_manager = QNetworkAccessManager()
		#self.network_manager.finished.connect(self.handle_response)

		# Add a menubar
		self.menu = self.menuBar()

		# Action buttons
	
		openButton = QAction("&Open file", self)
		openButton.triggered.connect(self.openFrom)
		saveButton = QAction("&Save file", self)
		saveButton.triggered.connect(self.saveTo)
		exportJSONButton = QAction("&Export to JSON", self)
		exportJSONButton.triggered.connect(self.exportToJSON)

		searchButton = QAction("&Search", self)
		searchButton.triggered.connect(self.searchButton)

		displayButton = QAction("Nb columns", self)

		# add menues
		self.file_menu = self.menu.addMenu("&File")
		self.edit_menu = self.menu.addMenu("&Edit")
		self.disp_menu = self.menu.addMenu("&Display")

		# Add actions to menues
		self.file_menu.addAction(openButton)
		self.file_menu.addAction(saveButton)
		self.file_menu.addAction(exportJSONButton)

		self.edit_menu.addAction(searchButton)
		
		self.disp_menu.addAction(displayButton)

		# Add widgets




		self.filePathLineEdit = QLineEdit()
		self.filePathLineEdit.setPlaceholderText("Enter a file path")
		self.openFileButton = QPushButton("Open file")
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
		

		# Attaching action to button
		self.openFileButton.clicked.connect(self.openFileFromButton)


	def switchToTab(self, index):
		self.tab.setCurrentIndex(index)


	def openFileFromButton(self):
		filepath = self.filePathLineEdit.text()
		self.openFile(filepath)

	def openFile(self, filepath):
		# open a file it it exists
		if (os.path.isfile(filepath)):
			page = PageWidget.PageWidget(filepath)
			filename = os.path.split(filepath)[-1]
			self.addTab(page, filename)
			self.filePathLineEdit.clear()


	def addTab(self, page, title):
		# add page to tab, with title as a title
		self.tab.addTab(page, title)
		index = self.tab.count()-1
		self.switchToTab(index)


	def removeTab(self, index):
		# remove the page at index
		page = self.tab.widget(index)
		self.tab.removeTab(index)


	def	openFrom(self):
		dialog = QFileDialog(self)
		dialog.setFileMode(QFileDialog.AnyFile)
		dialog.setViewMode(QFileDialog.Detail)
		if dialog.exec():
			filenames = dialog.selectedFiles()
		else:
			filenames = []
		print("open from: "+", ".join(filenames))
		for filename in filenames:
			self.openFile(filename)


	def saveTo(self):
		current_widget = self.tab.currentWidget() # get current widget
		if current_widget is not None:
			filepath = current_widget.file.filepath
			print("save to file :", filepath)
			dialog = QFileDialog(self)
			dialog.setFileMode(QFileDialog.AnyFile)
			dialog.setViewMode(QFileDialog.Detail)

			

	def exportToJSON(self):
		print("export to JSON")

	def searchButton(self):
		print("search button")

	def handle_response(self, reply):
		"""
		elapsed_time = time.time() - self.start_time
		self.send_button.setEnabled(True) # enable the button
		self.info_text.append(f"Response Time : {elapsed_time:.2f} seconds")
		if reply.error() == QNetworkReply.NoError:
			status_code = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
			self.info_text.append(f"HTTP error code: {status_code}")

			content = reply.readAll().data().decode("utf-8")
			self.response_text.setPlainText(content)

			headers = reply.rawHeaderList()
			for header in headers:
				header_cell = QTableWidgetItem(header.data().decode("utf-8"))
				value_cell = QTableWidgetItem(reply.rawHeader(header).data().decode("utf-8"))

				self.header_table.insertRow(self.header_table.rowCount())
				self.header_table.setItem(self.header_table.rowCount()-1, 0, header_cell)
				self.header_table.setItem(self.header_table.rowCount()-1, 1, value_cell)


		else:
			self.info_text.append("Error: "+reply.errorString())
		"""

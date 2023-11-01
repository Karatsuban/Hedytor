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
		#self.setMinimumSize(600,500)

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


		# Add widgets


		self.filePathLineEdit = QLineEdit()
		self.filePathLineEdit.setPlaceholderText("Enter a file path")
		self.openFileButton = QPushButton("Open file")
		self.networkFileCheckBox = QCheckBox("Network file")

		

		self.hexEditorTextEdit = QTextEdit()
		self.textEditorTextEdit = QTextEdit()

		# Add widgets to layout

		firstRowLayout = QHBoxLayout()
		layout.addLayout(firstRowLayout)
		
		secondRowLayout = QHBoxLayout()
		layout.addLayout(secondRowLayout)
		

		firstRowLayout.addWidget(self.filePathLineEdit)
		firstRowLayout.addWidget(self.openFileButton)
		firstRowLayout.addWidget(self.networkFileCheckBox)

		self.tab = QTabWidget(self) # tab widget
		self.tab.setMovable(True)
		self.tab.setTabsClosable(True)

		layout.addWidget(self.tab)
		# set action when closing the tab index
		self.tab.tabCloseRequested.connect(lambda index: self.removeTab(index))
		

		#self.newTab("blank")

		# Attaching action to button
		self.openFileButton.clicked.connect(self.openFile)


	def switchToTab(self, index):
		self.tab.setCurrentIndex(index)


	def openFile(self):
		# open a file it it exists
		filename = self.filePathLineEdit.text()
		if (os.path.isfile(filename)):
			page = PageWidget.PageWidget(filename)
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









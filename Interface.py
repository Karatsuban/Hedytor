import sys
import os
import time
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtNetwork import *



class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setMinimumSize(600,500)

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

		self.textEditorTextEdit = QTextEdit()
		self.hexEditorTextEdit = QTextEdit()

		# Add widgets to layout

		firstRowLayout = QHBoxLayout()
		layout.addLayout(firstRowLayout)
		
		secondRowLayout = QHBoxLayout()
		layout.addLayout(secondRowLayout)
		

		firstRowLayout.addWidget(self.filePathLineEdit)
		firstRowLayout.addWidget(self.openFileButton)
		firstRowLayout.addWidget(self.networkFileCheckBox)

	
		secondRowLayout.addWidget(self.textEditorTextEdit)
		secondRowLayout.addWidget(self.hexEditorTextEdit)



		# Attaching action to button

		self.openFileButton.clicked.connect(self.openFile)

	

	def openFile(self):
		filename = self.filePathLineEdit.text()
		if (os.path.isfile(filename)):
			print(os.path.getsize(filename), os.path.getmtime(filename), os.path.getctime(filename))
		print("Opening file!")


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


app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("Hedytor")
window.show()

app.exec()





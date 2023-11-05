from PySide6.QtWidgets import *
import json

class ExportWindow(QWidget):
	
	def __init__(self, data):
		super().__init__()
		self.layout = QVBoxLayout()
		self.data = data # data is a dictionary

		self.dataPrintable = ""
		for key, val in self.data.items():
			self.dataPrintable += str(key)+": "+str(val)+"\n"

		self.dataDisplay = QTextEdit()
		self.dataDisplay.setText(self.dataPrintable)

		self.layout.addWidget(self.dataDisplay)

		self.exportButton = QPushButton("Export to Json")
		self.exportButton.clicked.connect(self.exportFromButton)
		self.layout.addWidget(self.exportButton)

		self.status = QStatusBar()
		self.layout.addWidget(self.status)

		self.setLayout(self.layout)

	def exportFromButton(self):
		dialog = QFileDialog(self)
		dialog.AcceptMode(QFileDialog.AcceptSave) # set for save mode
		dialog.setFileMode(QFileDialog.AnyFile)
		dialog.setViewMode(QFileDialog.Detail)
		if dialog.exec():
			filenames = dialog.selectedFiles()
		else:
			filenames = []
		if (len(filenames) != 0):
			self.exportToJSON(filenames[0])

	def close(self):
		self.dataDisplay.close()
		super().close()

	def exportToJSON(self, filepath):

		jsoned_data = json.dumps(self.data)
		
		with open(filepath, "w") as file:
			try:
				json.dump(jsoned_data, file)
			except:
				self.status.showMessage("Error when writing!", 3000)
			else:
				self.status.showMessage("Write complete!", 3000)

		



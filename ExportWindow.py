from PySide6.QtWidgets import QApplication, QTextEdit, QWidget

class ExportWindow(QWidget):
	
	def __init__(self, data):
		super().__init__()
		layout = QVBoxLayout()
		self.data = data

		self.dataDisplay = QTextEdit()

		layout.addWidget(self.dataDisplay)
		self.setLayout(self.layout)



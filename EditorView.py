from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class EditorView(QTableView):
	
	def __init__(self, parent=None):
		super().__init__()
		self.parent = parent
	

	def event(self, event):
		if event.type() == QEvent.KeyPress:
			keyEvent = QKeyEvent(event)
			if keyEvent.key() in [Qt.Key_Delete, Qt.Key_Backspace]:
				self.deleteDataAt()	
				return True
		return super().event(event)


	def deleteDataAt(self):
		self.model().deleteDataAt(self.currentIndex())
		self.repaint()

from PySide6.QtWidgets import QApplication
import Interface
import sys

def main():
	print("Working")
	app = QApplication(sys.argv)
	window = Interface.MainWindow()
	window.setWindowTitle("Hedytor")
	window.show()
	app.exec()




if __name__ == "__main__":
	main()

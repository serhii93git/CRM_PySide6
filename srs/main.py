import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from srs.menu import setup_menu

class MainWindow(QMainWindow):
    """Create app Main Window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My SRM') # set up app name
        self.setGeometry(300, 300, 600, 400) #  set up window size and position

        setup_menu(self) # initial menu from 'menu.py'

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())




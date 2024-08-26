import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar

from srs.menu import setup_menu
from srs.central_widget import central_widget_show

class MainWindow(QMainWindow):
    """Create app Main Window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My SRM') # set up app name
        self.setGeometry(300, 300, 600, 400) #  set up window size and position

        setup_menu(self) #  initial menu from 'menu.py'
        #  self.add_button, self.edit_button, self.delete_button, self.table = central_widget_show(self)
        central_widget_show(self)  # initial central widget from 'central_widget.py'

        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage('Done')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())




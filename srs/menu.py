from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidget
from PySide6.QtGui import QAction


def setup_menu(window: QMainWindow):
    """Create menu bar"""

    #  create menu 'File'
    file_menu = window.menuBar().addMenu('File') #  add new 'File' button in menu bar
    action_exit = QAction('Exit', window) #  add new 'Exit' btn in 'File' menu
    action_exit.triggered.connect(window.close) #  set up action (window.close) for 'Exit' btn
    file_menu.addAction(action_exit) #  init (action_exit) in (file_menu) -> 'Exit' btn in 'File' menu

    #  create menu 'Help'
    file_help = window.menuBar().addMenu('Help')
    action_about = QAction('About', window)
    action_about.triggered.connect(lambda: show_about_dialog_window(window)) #  set up action for 'About' menu btn
    file_help.addAction(action_about)

#  create 'About App' dialog window for 'About' menu
def show_about_dialog_window(window):
    about_msg = QMessageBox(window)
    about_msg.setWindowTitle('About App')
    about_msg.setText('Simple SRM app run on PySide 6\nVersion: 0.0.01/alpha') #  set 'About App' text
    about_msg.setIcon(QMessageBox.Icon.Information) #  set icon for (about-msg) from base lib
    about_msg.exec() #  (about_msg) execution command

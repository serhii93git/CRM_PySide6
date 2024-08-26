from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
from sqlalchemy import table


#  create central widget
def central_widget_show(window):
    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    # create a layout for central widget
    layout = QVBoxLayout()
    central_widget.setLayout(layout)

    #  create table
    table = QTableWidget() #  set up widget type to table
    table.setColumnCount(4) #  set up column count
    table.setHorizontalHeaderLabels(['ID', 'Name', 'Phone', 'Address']) #  set up columns labels
    layout.addWidget(table) #  add table to layout

    #  add buttons
    add_button = QPushButton('Add')
    edit_button = QPushButton('Edit')
    delete_button = QPushButton('Delete')

    layout.addWidget(add_button)
    layout.addWidget(edit_button)
    layout.addWidget(delete_button)









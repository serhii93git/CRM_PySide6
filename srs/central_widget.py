from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QTableWidget,
                               QTableWidgetItem, QLineEdit, QFormLayout, QDialog,
                               QLabel, QDialogButtonBox)



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
    table.setHorizontalHeaderLabels(['Client_ID', 'Name', 'Phone', 'Address']) #  set up columns labels
    layout.addWidget(table) #  add table to layout

    #  add buttons

    add_button = QPushButton('Add') # create ADD button
    add_button.clicked.connect(lambda: add_button_dialog_window(window, table))

    edit_button = QPushButton('Edit')
    delete_button = QPushButton('Delete')

    layout.addWidget(add_button)
    layout.addWidget(edit_button)
    layout.addWidget(delete_button)

#  add dialog window for add new data in the table
def add_button_dialog_window(window, table):
    dialog = QDialog(window)
    dialog.setWindowTitle('Add new customer')
    form_layout = QFormLayout(dialog)

    id_input = QLineEdit(dialog)
    name_input = QLineEdit(dialog)
    phone_input = QLineEdit(dialog)
    address_input = QLineEdit(dialog)

    form_layout.addRow(QLabel('ID'), id_input)
    form_layout.addRow(QLabel('Name'), name_input)
    form_layout.addRow(QLabel('Phone'), phone_input)
    form_layout.addRow(QLabel('Address'), address_input)

    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
    form_layout.addWidget(button_box)

    button_box.accepted.connect(lambda: add_row_to_table(dialog, table, id_input.text(), name_input.text(),
                                                         phone_input.text(), address_input.text()))
    button_box.rejected.connect(dialog.reject)

    dialog.exec()


def add_row_to_table(dialog, table, id_text, name_text, phone_text, address_text):
    row_position = table.rowCount()
    table.insertRow(row_position)
    table.setItem(row_position, 0, QTableWidgetItem(id_text))
    table.setItem(row_position, 1, QTableWidgetItem(name_text))
    table.setItem(row_position, 2, QTableWidgetItem(phone_text))
    table.setItem(row_position, 3, QTableWidgetItem(address_text))

    dialog.accept()



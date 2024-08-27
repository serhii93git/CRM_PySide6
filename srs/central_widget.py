from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QTableWidget,
                               QTableWidgetItem, QLineEdit, QFormLayout, QDialog,
                               QLabel, QDialogButtonBox, QMessageBox, QHBoxLayout)



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

    #  create buttons
    button_layout = QHBoxLayout() #  create layout for buttons


    add_button = QPushButton('Add') # create ADD button
    add_button.clicked.connect(lambda: add_button_dialog_window(window, table)) #  set up func for (add_button) btn

    edit_button = QPushButton('Edit')
    edit_button.clicked.connect(lambda: edit_dialog_window(window, table))

    delete_button = QPushButton('Delete')
    delete_button.clicked.connect(lambda: delete_selected_row(window, table))

    #  init buttons with (buttons_layout)
    button_layout.addWidget(add_button)
    button_layout.addWidget(edit_button)
    button_layout.addWidget(delete_button)

    layout.addLayout(button_layout) #  init buttons layout

#  add dialog window for input new data
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

#  add input data in the table
def add_row_to_table(dialog, table, id_text, name_text, phone_text, address_text):
    row_position = table.rowCount()
    table.insertRow(row_position)
    table.setItem(row_position, 0, QTableWidgetItem(id_text))
    table.setItem(row_position, 1, QTableWidgetItem(name_text))
    table.setItem(row_position, 2, QTableWidgetItem(phone_text))
    table.setItem(row_position, 3, QTableWidgetItem(address_text))

    dialog.accept() #  close dialog window after OK btn pressed

#  add dialog window for edit data
def edit_dialog_window(window, table):
    selected_row = table.currentRow()
    if selected_row < 0:
        QMessageBox.warning(window, 'Warning', 'Please, select line to edit')
        return

    dialog = QDialog(window)
    dialog.setWindowTitle('Edit customer info')
    form_layout = QFormLayout(dialog)

    id_input = QLineEdit(dialog)
    name_input = QLineEdit(dialog)
    phone_input = QLineEdit(dialog)
    address_input = QLineEdit(dialog)

    #  get data from selected line
    id_input.setText(table.item(selected_row, 0).text())
    name_input.setText(table.item(selected_row, 1).text())
    phone_input.setText(table.item(selected_row, 2).text())
    address_input.setText(table.item(selected_row, 3).text())

    form_layout.addRow(QLabel('Client_ID:'), id_input)
    form_layout.addRow(QLabel('Name:'), name_input)
    form_layout.addRow(QLabel('Phone:'), phone_input)
    form_layout.addRow(QLabel('Address:'), address_input)

    button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
    form_layout.addWidget(button_box)

    button_box.accepted.connect(lambda: edit_table_row(dialog, table, selected_row, id_input.text(),
                                                       name_input.text(), phone_input.text(), address_input.text()))

    button_box.rejected.connect(dialog.reject)

    dialog.exec()

def edit_table_row(dialog, table, row, id_text, name_text, phone_text, address_text):
    table.setItem(row, 0, QTableWidgetItem(id_text))
    table.setItem(row, 1, QTableWidgetItem(name_text))
    table.setItem(row, 2, QTableWidgetItem(phone_text))
    table.setItem(row, 3, QTableWidgetItem(address_text))

    dialog.accept()


def delete_selected_row(window, table):
    selected_row = table.currentRow()
    if selected_row < 0:
        QMessageBox.warning(window, 'Warning', 'Please, select line to delete')
        return
    table.removeRow(selected_row)






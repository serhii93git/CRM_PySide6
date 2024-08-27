from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QTableWidget,
                               QTableWidgetItem, QLineEdit, QFormLayout, QDialog,
                               QLabel, QDialogButtonBox, QMessageBox, QHBoxLayout)
from db_settings import Customer
from srs.db_settings import session


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

    load_data_from_db(table)

def load_data_from_db(table):
    customers = session.query(Customer).all()
    table.setRowCount(0)
    for customer in customers:
        row_position = table.rowCount()
        table.insertRow(row_position)
        table.setItem(row_position, 0, QTableWidgetItem(str(customer.id)))
        table.setItem(row_position, 1, QTableWidgetItem(str(customer.name)))
        table.setItem(row_position, 2, QTableWidgetItem(str(customer.phone)))
        table.setItem(row_position, 3, QTableWidgetItem(str(customer.address)))


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

    #  add line in to database
    new_customer = Customer(id=int(id_text), name=name_text, phone=phone_text, address=address_text)
    session.add(new_customer)
    session.commit()

    #  add line in to app
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
    #  get data from the database to edit
    customer = session.query(Customer).filter(Customer.id == int(id_text)).first()
    if customer:
        customer.name = name_text
        customer.phone = phone_text
        customer.address = address_text
        session.commit()

    #  get data from table to edit
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

    #  delete line from database
    id_item = table.item(selected_row, 0)
    if id_item:
        customer_id = int(id_item.text())
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        table.removeRow(selected_row)
    else:
        QMessageBox.warning(window, 'Error', 'Customer not found in database')






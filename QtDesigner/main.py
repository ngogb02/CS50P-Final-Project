import sys
from PySide6 import QtWidgets


from My_House_Inventory import My_House_Inventory


app = QtWidgets.QApplication(sys.argv)

window = My_House_Inventory()

window.show()
app.exec()

#pyside6-uic My_House_Inventory.ui > ui_My_House_Inventory.py
#pyside6-rcc resource.qrc -o resource_rc.py

#
#pyside6-rcc resource.qrc -pyside6-uic My_House_Inventory_01.ui > ui_My_House_Inventory_01.pyo resource_rc.py
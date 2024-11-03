import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader() #Set up a loader object

app = QtWidgets.QApplication(sys.argv)
window = loader.load("My_House_Inventory.ui", None) #Load the ui - happens at run time!

def add():
    print(f"add item: {window.Add_Item_Line_Edit.text()}")
    window.Add_Item_Line_Edit.clear()
def remove():
    print(f"remove item: {window.Remove_Item_Line_Edit.text()}")
    window.Remove_Item_Line_Edit.clear()
def create():
    print(f"create item: {window.Create_Item_Line_Edit.text()}")
    window.Create_Item_Line_Edit.clear()

#Changing the properties in the form
window.setWindowTitle("My House Inventory")

#Accessing widgets in the form
window.Add_Item_Button.clicked.connect(add)
window.Remove_Item_Button.clicked.connect(remove)
window.Create_An_Item_Button.clicked.connect(create)
window.show()
app.exec()
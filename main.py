import sys
from PySide6 import QtWidgets
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt


from My_House_Inventory import My_House_Inventory


app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

# Create a light palette because by default, PySide6 will inherit the dark mod set by linux/window, turning the GUI dark.
light_palette = QPalette()
light_palette.setColor(QPalette.Window, QColor(255, 255, 255))  # Main background
light_palette.setColor(QPalette.WindowText, Qt.black)
light_palette.setColor(QPalette.Base, QColor(255, 255, 255))  # Input fields background
light_palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
light_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
light_palette.setColor(QPalette.ToolTipText, Qt.black)
light_palette.setColor(QPalette.Text, Qt.black)
light_palette.setColor(QPalette.Button, QColor(255, 255, 255))  # Button background
light_palette.setColor(QPalette.ButtonText, Qt.black)
light_palette.setColor(QPalette.BrightText, Qt.red)
light_palette.setColor(QPalette.Link, QColor(0, 0, 255))
light_palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
light_palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))

app.setPalette(light_palette)
                                               
window = My_House_Inventory()

window.show()
app.exec()

#pyside6-uic My_House_Inventory_01.ui > ui_My_House_Inventory_01.py
#pyside6-rcc resource.qrc -o resource_rc.py
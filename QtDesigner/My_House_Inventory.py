import resource_rc 
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QDateTimeEdit
from PySide6.QtGui import QIcon, QPixmap
from ui_My_House_Inventory import Ui_My_House_Inventory

class My_House_Inventory(QWidget, Ui_My_House_Inventory):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("My House Inventory")
        self.Add_Item_Button.clicked.connect(self.add)
        self.Remove_Item_Button.clicked.connect(self.remove)
        self.Create_An_Item_Button.clicked.connect(self.create)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        
        plus_icon = QIcon(":/newPrefix/images/add-to-cart.png")
        minus_icon = QIcon(":/newPrefix/images/subtract-of-shopping-cart.png")
        create_icon = QIcon(":/newPrefix/images/optimization.png")
        window_icon = QIcon(":/newPrefix/images/building.png")
       
        date_time_icon = QPixmap(":/newPrefix/images/timetable.png").scaled(20, 20, Qt.KeepAspectRatio)
        self.Date_Time_Title.setPixmap(date_time_icon)
        self.Date_Time_Title.setAlignment(Qt.AlignRight)
        layout = QHBoxLayout(self.Date_Time_Title)


        self.Add_Item_Button.setIcon(plus_icon)
        self.Remove_Item_Button.setIcon(minus_icon)
        self.Create_An_Item_Button.setIcon(create_icon)
        self.setWindowIcon(window_icon)
        self.Date_Time_Title.setPixmap(date_time_icon)


    def add(self):
        print(f"add item: {self.Add_Item_Line_Edit.text()}")
        self.Add_Item_Line_Edit.clear()
    def remove(self):
        print(f"remove item: {self.Remove_Item_Line_Edit.text()}")
        self.Remove_Item_Line_Edit.clear()
    def create(self):
        print(f"create item: {self.Create_Item_Line_Edit.text()}")
        self.Create_Item_Line_Edit.clear()
#COPILOT CODE
# import json
# from PySide6.QtCore import QAbstractTableModel, Qt, QDateTime, QFileSystemWatcher
# from PySide6.QtWidgets import QWidget, QTableView, QTabWidget, QHBoxLayout
# from PySide6.QtGui import QIcon, QPixmap
# from ui_My_House_Inventory import Ui_My_House_Inventory

# class My_House_Inventory(QWidget, Ui_My_House_Inventory):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         self.setWindowTitle("My House Inventory")
#         self.Add_Item_Button.clicked.connect(self.add)
#         self.Remove_Item_Button.clicked.connect(self.remove)
#         self.Create_An_Item_Button.clicked.connect(self.create)
#         self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

#         # Set icons
#         plus_icon = QIcon(":/newPrefix/images/add-to-cart.png")
#         minus_icon = QIcon(":/newPrefix/images/subtract-of-shopping-cart.png")
#         create_icon = QIcon(":/newPrefix/images/optimization.png")
#         window_icon = QIcon(":/newPrefix/images/building.png")
#         date_time_icon = QPixmap(":/newPrefix/images/timetable.png").scaled(20, 20, Qt.KeepAspectRatio)

#         self.Add_Item_Button.setIcon(plus_icon)
#         self.Remove_Item_Button.setIcon(minus_icon)
#         self.Create_An_Item_Button.setIcon(create_icon)
#         self.setWindowIcon(window_icon)
#         self.Date_Time_Title.setPixmap(date_time_icon)
#         self.Date_Time_Title.setAlignment(Qt.AlignRight)

#         layout = QHBoxLayout(self.Date_Time_Title)

#         # Load JSON data
#         self.data_path = 'path/to/test_inventory.json'  # Adjust the path as needed
#         self.data = self.load_json(self.data_path)
        
#         # QFileSystemWatcher to monitor the JSON file
#         self.file_watcher = QFileSystemWatcher([self.data_path])
#         self.file_watcher.fileChanged.connect(self.on_file_changed)

#         # Populate the tabs
#         self.populate_tabs(self.data)

#     def load_json(self, filename):
#         with open(filename, 'r') as file:
#             return json.load(file)

#     def add(self):
#         print(f"add item: {self.Add_Item_Line_Edit.text()}")
#         self.Add_Item_Line_Edit.clear()

#     def remove(self):
#         print(f"remove item: {self.Remove_Item_Line_Edit.text()}")
#         self.Remove_Item_Line_Edit.clear()

#     def create(self):
#         print(f"create item: {self.Create_Item_Line_Edit.text()}")
#         self.Create_Item_Line_Edit.clear()

#     def populate_tabs(self, data):
#         tab_widget = self.findChild(QTabWidget, 'yourTabWidgetObjectName')  # Replace with your object name
#         tab_widget.clear()  # Clear existing tabs

#         for category, items in data.items():
#             model = InventoryModel(items)

#             table_view = QTableView()
#             table_view.setModel(model)

#             # Customize the QTableView
#             table_view.horizontalHeader().setStretchLastSection(True)
#             table_view.setAlternatingRowColors(True)
#             table_view.setSelectionBehavior(QTableView.SelectRows)
#             table_view.setSelectionMode(QTableView.SingleSelection)

#             tab_widget.addTab(table_view, category)

#     def on_file_changed(self):
#         self.data = self.load_json(self.data_path)
#         self.populate_tabs(self.data)

# # Main execution
# if __name__ == '__main__':
#     from PySide6.QtWidgets import QApplication
#     import sys

#     app = QApplication(sys.argv)
#     window = My_House_Inventory()
#     window.show()
#     sys.exit(app.exec())

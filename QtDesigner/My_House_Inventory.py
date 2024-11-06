import resource_rc, json
from PySide6.QtCore import Qt, QDateTime, QAbstractTableModel, QModelIndex, QFileSystemWatcher
from PySide6.QtWidgets import QWidget, QHBoxLayout, QStyledItemDelegate
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

        #PART OF TABLVIEW CUSTOM TABLE CONSTRUCTION - 1.0: set file path and call load_json()
        #At this step, self.data looks like this:
        #{'Fruits': 
        #     {'Apple': {'_location': 'Fridge', '_quantity': 40, '_date': '10/10/2023', 'barcode': None, 'price': None}, 
        #     'Banana': {'_location': 'Fridge', '_quantity': 56, '_date': '10/10/2024', 'barcode': None, 'price': None}, 
        #     'Mango': {'_location': 'Fridge', '_quantity': 100, '_date': '10/08/2026', 'barcode': None, 'price': None}, 
        #     'Strawberry': {'_location': 'Fridge', '_quantity': 69, '_date': '10/27/2024', 'barcode': None, 'price': None}}, 
        # 'Ingredients': {}}
        self.data_path = '/home/baongo/Documents/Project/inventory.json' 
        self.data = self.load_json(self.data_path)

        #QFileSystemWatcher to monitor the JSON file - 1.1
        self.file_watcher = QFileSystemWatcher([self.data_path])
        self.file_watcher.fileChanged.connect(self.on_file_changed)
        

    def add(self):
        print(f"add item: {self.Add_Item_Line_Edit.text()}")
        self.Add_Item_Line_Edit.clear()
    def remove(self):
        print(f"remove item: {self.Remove_Item_Line_Edit.text()}")
        self.Remove_Item_Line_Edit.clear()
    def create(self):
        print(f"create item: {self.Create_Item_Line_Edit.text()}")
        self.Create_Item_Line_Edit.clear()

    #PART OF TABLVIEW CUSTOM TABLE CONSTRUCTION - 1.0: LOAD JSON DATA
    def load_json(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)
    
    #Reload the data by calling load_json() again, and then pupulate_tabs() calls the data again to shows the changes in the JSON file - 1.1
    def on_file_changed(self):
        self.data = self.load_json(self.data_path)
        self.populate_tabs(self.data)

    


class InventoryModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._header = ['Item Name', 'Quantity', 'Location', 'Date']

    def rowCount(self, panrets = None):
        return len(self._data) #
    
    def columnCount(self, parents = None):
        return len(self._header) # number of header (4): Item Name, Quantity, Location, Date

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            #data.keys() will give a list of the keys, in thise case, the fruits (apple, banana, mango)
            item_name = list(self._data.keys())[index.row()]
            item_details = self._data[item_name]
            if index.column() == 0
                return item_name
            elif index.column() == 1
                return item_details['_quantity']
            elif index.column() == 2
                return item_details['_location']
            elif index.column() == 3
                return item_details['_date']
        return None




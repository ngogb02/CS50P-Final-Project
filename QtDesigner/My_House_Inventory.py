import resource_rc, json
from PySide6.QtCore import Qt, QDateTime, QAbstractTableModel, QFileSystemWatcher
from PySide6.QtWidgets import QWidget, QHBoxLayout, QTableView, QTabWidget, QHeaderView
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
        #window_icon = QIcon(":/newPrefix/images/building.png") 

        date_time_icon = QPixmap(":/newPrefix/images/timetable.png").scaled(20, 20, Qt.KeepAspectRatio)
        self.Date_Time_Title.setPixmap(date_time_icon)
        self.Date_Time_Title.setAlignment(Qt.AlignRight)
        layout = QHBoxLayout(self.Date_Time_Title)

        self.Add_Item_Button.setIcon(plus_icon)
        self.Remove_Item_Button.setIcon(minus_icon)
        self.Create_An_Item_Button.setIcon(create_icon)
        #self.setWindowIcon(window_icon)
        self.Date_Time_Title.setPixmap(date_time_icon)

        # PART OF TABLEVIEW CUSTOM TABLE CONSTRUCTION - 1.0: set file path and call load_json()
        # At this step, self.data looks like this:
        # {'Fruits':
        #     {'Apple': {'_location': 'Fridge', '_quantity': 40, '_date': '10/10/2023', 'barcode': None, 'price': None}, 
        #     'Banana': {'_location': 'Fridge', '_quantity': 56, '_date': '10/10/2024', 'barcode': None, 'price': None}, 
        #     'Mango': {'_location': 'Fridge', '_quantity': 100, '_date': '10/08/2026', 'barcode': None, 'price': None}, 
        #     'Strawberry': {'_location': 'Fridge', '_quantity': 69, '_date': '10/27/2024', 'barcode': None, 'price': None}}, 
        # 'Ingredients': {}}
        self.data_path = 'inventory.json'
        self.data = self.load_json(self.data_path)

        # QFileSystemWatcher to monitor the JSON file - 1.1
        # this will ensure anytime the JSON is updated with new info, this will get notified and call on_file_changed()
        # to reload the json data using load_json() and repopulate the tableview.
        self.file_watcher = QFileSystemWatcher([self.data_path])
        self.file_watcher.fileChanged.connect(self.on_file_changed)

        #call the function populate tab, feeding in arugment self.data (which is the json info)
        self.populate_tab(self.data)


    def add(self):
        print(f"add item: {self.Add_Item_Line_Edit.text()}")
        self.Add_Item_Line_Edit.clear()

    def remove(self):
        print(f"remove item: {self.Remove_Item_Line_Edit.text()}")
        self.Remove_Item_Line_Edit.clear()

    def create(self):
        print(f"create item: {self.Create_Item_Line_Edit.text()}")
        self.Create_Item_Line_Edit.clear()

    # PART OF TABLEVIEW CUSTOM TABLE CONSTRUCTION - 1.0: LOAD JSON DATA
    def load_json(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    # Reload the data by calling load_json() again, and then pupulate_tabs() calls the data again to shows the changes in the JSON file - 1.1
    def on_file_changed(self):
        self.data = self.load_json(self.data_path)
        self.populate_tabs(self.data)

    def populate_tab(self, data):
        # The findChild method is used to find a child widget with a specific name and type.
        # The clear method removes all the existing tabs from the QTabWidget.
        tab_widget = self.findChild(QTabWidget, 'CategoryTabWidget')
        tab_widget.clear() #clear existing tabs

        for category, items in data.items():
            # Create an instance of the class InventoryModel with the current items. 
            # This model handles the data for QTableView.
            model = InventoryModel(items)   
            # Create a new QTableView instance to display the data.
            table_view = QTableView()
            # Set the InventoryModel(items) as the data model for QTableView
            # the model should inherit from QAbstractTableModel or any other desired model.
            table_view.setModel(model)

            # Customize the QTableView
            # Stretches the last section of the horizontal header to fill the available space.
            table_view.horizontalHeader().setStretchLastSection(True)
            # Enables alternating row colors for better readability.
            table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            # Configures the selection behavior to select entire rows.
            table_view.setSelectionBehavior(QTableView.SelectRows)
            # Sets the selection mode to single selection, allowing only one row to be selected at a time.
            table_view.setSelectionMode(QTableView.SingleSelection)

    
            # Adds the child widget QTableView to the QTabWidget. 
            # The tab is labeled with the category name.
            tab_widget.addTab(table_view, category)

class InventoryModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        # Note that when data is passed in by the populate_tab(), it passes in data[category], so the structure will be
        # in this case it would be data['Fruits'] and the data passed in would look like:
        # like ={ 'apple': {Loc, Qty, Date, ...},
        #        'banana': {Loc, Qty, Date, ...},
        #        'mango' : {Loc, Qty, Date, ...}
        #        }
        self._data = data
        self._header = ['Item Name', 'Quantity', 'Location', 'Date']

    def rowCount(self, parents=None):
        return len(self._data)  # this will return the len# in term of how many keys are in the data.

    def columnCount(self, parents=None):
        return len(self._header)  # number of header (4): Item Name, Quantity, Location, Date

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            # data.keys() will give a list of the keys, in this case, the fruits (apple, banana, mango)
            # this will return the key, in this case, {apple, banana, ...}
            # This part uses the row number obtained from index.row() to access the corresponding element in the list of keys.
            # in this case, if index.row() is 0, then it would be self._data.keys()[0], which is indexing 'apple'
            item_name = list(self._data.keys())[index.row()]
            item_details = self._data[item_name]
            if index.column() == 0:
                return item_name
            elif index.column() == 1:
                return item_details['_quantity']
            elif index.column() == 2:
                return item_details['_location']
            elif index.column() == 3:
                return item_details['_date']
        return None

    # Orientation: Can be either Qt.Horizontal for column headers or Qt.Vertical for row headers.
    # section: The section index of the header (i.e., the row or column number).
    # use headerData(), to provide header data, like titles of columns or rows, to the view.
    # user setHeaderDara(), to make the header editable during runtime [do not use in this case].
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._header[section]
        return None # Use None to indicate no data for other roles



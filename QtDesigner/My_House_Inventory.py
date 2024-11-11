import resource_rc, json
from PySide6.QtCore import Qt, QDateTime, QAbstractTableModel, QFileSystemWatcher, QRegularExpression, QEvent, QObject
from PySide6.QtWidgets import QWidget, QHBoxLayout, QTableView, QTabWidget, QHeaderView, QLineEdit
from PySide6.QtGui import QIcon, QPixmap, QRegularExpressionValidator
#from ui_My_House_Inventory import Ui_My_House_Inventory
from ui_My_House_Inventory_01 import Ui_My_House_Inventory # Test line

class My_House_Inventory(QWidget, Ui_My_House_Inventory):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("My House Inventory")
        self.Add_Item_Button.clicked.connect(self.add)
        self.Remove_Item_Button.clicked.connect(self.remove)
        #self.Create_An_Item_Button.clicked.connect(self.create)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        # Test Code - GroupBox - Pushbutton - 3 Lines Edit
        self.Create_An_Item_Button.clicked.connect(self.quantity_location_date)
        
        # Test Code - regex / event-filter for inputting Date
        # regex = QRegularExpression(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$")
        # validator = QRegularExpressionValidator(regex)
        # self.Create_Item_Date_Line_Edit.setValidator(validator)

        # Install a custom event filter for automatic slashes insertion when typing in date
        self.date_input_filter = QLineEdit(self)
        self.Create_Item_Date_Line_Edit.installEventFilter(DateInputFilter(self.date_input_filter))


        date_time_icon = QPixmap(":/newPrefix/images/timetable.png").scaled(20, 20, Qt.KeepAspectRatio)
        self.Date_Time_Title.setPixmap(date_time_icon)
        self.Date_Time_Title.setAlignment(Qt.AlignRight)
        layout = QHBoxLayout(self.Date_Time_Title)

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

    # Test Code - GroupBox - Pushbutton - 3 Lines Edit
    def quantity_location_date(self):
        Item_name = self.Create_Item_Item_Name_Line_Edit.text()
        quantity = self.Create_Item_Quantity_Line_Edit.text()
        location = self.Location_comboBox.currentText()
        date = self.Create_Item_Date_Line_Edit.text()
        print(Item_name)
        print(quantity)
        print(location)
        print(date)
        self.Create_Item_Item_Name_Line_Edit.clear()
        self.Create_Item_Quantity_Line_Edit.clear()
        self.Create_Item_Date_Line_Edit.clear()

    # Define a new class that inherits from QObject - for even filter of Date input. 

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


class DateInputFilter(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Define the regular expression for the date format MM/DD/YYYY
        final_regex = QRegularExpression(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$")
        self.final_validator = QRegularExpressionValidator(final_regex, self) 
        
    # Override the eventFilter function, intercept events sent to obj and allows custom processing of those events.
    def eventFilter(self, obj, event):
        # Check if the type of the event is a key press event
        if event.type() == QEvent.KeyPress:
            # Retrieve the key code that is pressed, like Qt.Key_0 (IT DOES NOT GIVE the text of the key like "0")
            key = event.key()
            print(f"event.key: {key}")
            # Retrieves the current text from the object (i.e Create_Item_Date_Line_Edit), if pressed Qt.Key_0 then it's "0"
            # Retrieve what's currently in the object, could be "01" or "01/05"... 
            text = obj.text()
            print(f"obj.text(): {text}")
            # Retrieve the current cursor position within the text
            cursor_position = obj.cursorPosition()
            print(f"cursor position: {cursor_position}")
            # Retrieve the text of the key pressed.
            char = event.text()
            print(f"event.text(): {char}")

            # Check if the key pressed is a numeric key (0-9) and if cursor position at 2 or 5 [MM/DD/YYYY] 
            if Qt.Key_0 <= key <= Qt.Key_9:
                # Insert the character at the current cursor position
                new_text = text[:cursor_position] + char + text[cursor_position:]
                new_cursor_position = cursor_position + 1
                print(f"new cursor position: {new_cursor_position}")
                print(f"new text: {new_text}")

                # Validate the new text
                if not self.is_valid_partial_date(new_text, new_cursor_position):
                    return True  # Ignore the key press if the new text is invalid

                if new_cursor_position in [2, 5]:
                    new_text = text[:new_cursor_position] + char + "/" + text[new_cursor_position:]
                    new_cursor_position += 1
                    print(f"new cursor position: {new_cursor_position}")
                    print(f"new text: {new_text}")
                
                if len(new_text) > 10:
                    return True

                obj.setText(new_text)
                obj.setCursorPosition(new_cursor_position)
                return True
            
        elif event.type() == QEvent.FocusOut:
            text = obj.text()
            state, _, _ = self.final_validator.validate(text, len(text))
            if state != QRegularExpressionValidator.Acceptable:
                print("Invalid final input")
            return False
        
        return super().eventFilter(obj, event)
    
    def is_valid_partial_date(self, text, cursor_position):
        # Validate the month part
        # If the cursor position is at 1 (after typing the first character)
        # Checks if the first char is either '0' or '1'
        if cursor_position == 1:
            # If return False, the caller will result in "if not False" -> "if True" -> execute if-block code -> return True (thus ignoring the user input)
            return text[0] in "01"
        # If cursor position is at 2 (after typing the second character)
        # Check if the first two char form a valid month (01 to 12)
        elif cursor_position == 2:
            return text[:2] in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        
        # Validate the day part
        # If the cursor position is at 4 (after typing the first char of the day)
        # Check if the first char of the day is '0', '1', '2', or '3' (valid starting digits for days)
        # Note that once the cursor position is at 2, the DateInputFilter automatically adds a "/" and then move the cursor position 1 to the right
        # When the text = "12" -> it automatically turns to -> "12/" -> when the user presses the 3rd number (i.e "3") -> it turns to "12/3" (cursor position now at 4)
        # index string of text starts at 0, for example "12/32/2024", text[3] = 3, text[2] = /, text[:2]  = 12 (not inclusive when using ":")
        elif cursor_position == 4:
            return text[3] in "0123"
        elif cursor_position == 5:
            # Retrieve the month from text.
            # Convert to int for performing "if in", otherwise "04" would not find in "[4, 6, 9, 11]".
            month = int(text[:2])
            # Retrieve the day from text.
            # Convert to int for performing "if in".
            day = int(text[3:5])
            # If months with 30 days (April (4), June (6), September (9), November (11))
            if month in [4, 6, 9, 11]:
                # If day is larger than 30, it would return False, resulting in "if not False" which is "if True", then the next code executes "return True", thus ignoring the input.
                return day <= 30
            # For Feburary, simplified, allow max to 29 days for leap year. 
            elif month == 2:
                return day <= 29  # Simplified, not checking for leap year
            # All other months have 31 days max. 
            else:
                return day <= 31
        # If all the "if's" here returns True, then the final line should return True, so that the caller becomes "if not true" = "if false", then it skips "return True" line,
        # Thus, moving onto the next lines of DataInputFilter.
        return True
    

class InventoryModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        # Note that when data is passed in by the populate_tab(), it passes in data[category], so the structure will be;
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



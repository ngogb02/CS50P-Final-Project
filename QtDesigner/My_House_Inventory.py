import resource_rc, json, sys, os, importlib, classes
from PySide6.QtCore import Qt, QDateTime, QAbstractTableModel, QFileSystemWatcher, QRegularExpression, QEvent, QObject
from PySide6.QtWidgets import QWidget, QHBoxLayout, QTableView, QTabWidget, QHeaderView, QPushButton, QMessageBox
from PySide6.QtGui import QPixmap, QRegularExpressionValidator
#from ui_My_House_Inventory import Ui_My_House_Inventory
from ui_My_House_Inventory_01 import Ui_My_House_Inventory

from project import *

class My_House_Inventory(QWidget, Ui_My_House_Inventory):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("My House Inventory")
        self.Adjust_Item_Button.clicked.connect(self.adjust)
        self.Remove_Item_Button.clicked.connect(self.remove)
        self.Create_An_Item_Button.clicked.connect(self.create_item_update_json)

        # When first launching GUI, the focus will be on the LineEdit
        self.Create_Item_Item_Name_Line_Edit.setFocus()
        
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm AP")

        # Test Code - regex / event-filter for inputting Date
        # regex = QRegularExpression(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$")
        # validator = QRegularExpressionValidator(regex)
        # self.Create_Item_Date_Line_Edit.setValidator(validator)

        # Install a custom event filter for automatic slashes insertion when typing in date to help users input the correct format
        self.date_input_filter = DateInputFilter(self)
        self.Create_Item_Date_Line_Edit.installEventFilter(self.date_input_filter)


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


        # Call the function populate tab, feeding in arugment self.data (which is the json info)
        # This function only activates once at the beginning of launch.
        # Function "on_file_changed" will be the one calling to re-populate everytime JSON is updated.
        self.populate_tab(self.data)


        # QFileSystemWatcher to monitor the JSON file - 1.1
        # this will ensure anytime the JSON is updated with new info, this will get notified and call on_file_changed()
        # to reload the json data using load_json() and repopulate the tableview.
        self.file_watcher = QFileSystemWatcher([self.data_path])
        self.file_watcher.fileChanged.connect(self.on_file_changed)


    # Test Code 
    def create_item_update_json(self):
        Item_name = self.Create_Item_Item_Name_Line_Edit.text()
        # qty needs to be convert to int because the funct create_item_class() in project.py expects an int. 
        quantity = int(self.Create_Item_Quantity_Line_Edit.text())  
        location = self.Location_comboBox.currentText()
        category = self.Category_comboBox.currentText()
        date = self.Create_Item_Date_Line_Edit.text()

        # print(Item_name)
        # print(quantity)
        # print(location)
        # print(date)

        # Call to project.py to create a custom class and an instance (object)
        create_item_class(Item_name, location, quantity, date)
        # Reload the classes.py file so that My_House_Inventory.py imports the updated version
        importlib.reload(importlib.import_module('classes'))
        item_class = self.Create_Item_Item_Name_Line_Edit.text().capitalize()
        # print(item_class)
        # print(type(item_class))
        item_object = getattr(classes, item_class.lower(), None)
        # print(item_object)
        # print(type(item_object))
        insert_items_into_inventory(category, item_object)
        update_inventoryJSON("inventory.json")
        remove_items_from_inventory(category, item_object)

        print(f'inventory from create item: {show_init_inventory()}')

        self.Create_Item_Item_Name_Line_Edit.clear()
        self.Create_Item_Quantity_Line_Edit.clear()
        self.Create_Item_Date_Line_Edit.clear()


    def adjust(self):
        filename = 'inventory.json'
        item_name = self.Create_Item_Item_Name_Line_Edit_3.text()
        Quantity = int(self.Create_Item_Quantity_Line_Edit_2.text())
        Date = self.Create_Item_Date_Line_Edit_2.text()
        Location = self.Location_comboBox_2.currentText()
        Category = self.Category_comboBox_3.currentText()   

        with open(filename, 'r') as file:
            json_data = json.load(file)

            for category, items in json_data.items():
                if Category in category and item_name in items:
                        if json_data[Category][item_name]['_quantity'] != Quantity:
                            json_data[Category][item_name]['_quantity'] = Quantity

                        if json_data[Category][item_name]['_location'] != Location:
                            json_data[Category][item_name]['_location'] = Location

                        if json_data[Category][item_name]['_date'] != Date:
                            json_data[Category][item_name]['_date'] = Date
            
            with open(filename, 'w') as file:
                json.dump(json_data, file, indent=4)

        self.Create_Item_Item_Name_Line_Edit_3.clear()
        self.Create_Item_Quantity_Line_Edit_2.clear()
        self.Create_Item_Date_Line_Edit_2.clear()


    def remove(self):
        item = self.Create_Item_Item_Name_Line_Edit_2.text()
        item_object = getattr(classes, item.lower(), None)
        filename = 'inventory.json'
        category = self.Category_comboBox_2.currentText()
        if item == "":
            if remove_category_from_JSON(filename, category) == False:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText("Warning: The category doesn't exist.")
                msg_box.setInformativeText("Specify a category that exist")
                msg_box.setWindowTitle("Warning")
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec()
            else:
                remove_category_from_JSON(filename, category)

        elif remove_item_from_JSON(filename, category, item_object) == None:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText(f"Warning: item: '{item}' or category '{category}' doesn't exist.")
            msg_box.setInformativeText("Specify an item/category that exist")
            msg_box.setWindowTitle("Warning")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
        else:
            item = self.Create_Item_Item_Name_Line_Edit_2.text()
            category = self.Category_comboBox_2.currentText()
            class_filename = 'classes.py'
            remove_item_from_JSON(filename, category, item_object)
            remove_item_from_file(class_filename, item.capitalize())
            self.Create_Item_Item_Name_Line_Edit_2.clear()


    # PART OF TABLEVIEW CUSTOM TABLE CONSTRUCTION - 1.0: LOAD JSON DATA
    def load_json(self, filename):
        # Note that the GUI will try to load up the json as soon as it's launched.
        # Check if the json file exist and not empty.
        if os.path.exists('inventory.json') and os.path.getsize('inventory.json') > 0:
            with open(filename, 'r') as file:
                return json.load(file)
        else:
            # Return an empty dictionary if file is empty or doesn't exist 
            return {}

    # Reload the data by calling load_json() again, and then pupulate_tabs() calls the data again to shows the changes in the JSON file - 1.1
    def on_file_changed(self):
        self.data = self.load_json(self.data_path)

        # Get the current CategoryTabWidget index that the user is currently on.
        current_tab_index = self.CategoryTabWidget.currentIndex()

        # Populate the tableview per new data.
        self.populate_tab(self.data)

        # Set the index tab to user's viewing tab, this will ensure that when the user makes an update to an item on a certain
        # Tab, the item will change but the focus will not change back to the initial tab, it will remain in the current view tab.
        self.CategoryTabWidget.setCurrentIndex(current_tab_index)

    def populate_tab(self, data):
        # The findChild method is used to find a child widget with a specific name and type.
        # The clear method removes all the existing tabs from the QTabWidget.
        tab_widget = self.findChild(QTabWidget, 'CategoryTabWidget')
        tab_widget.clear() #clear existing tabs
        if data == {}:
            model = InventoryModel(None)
            table_view = QTableView()
            table_view.setModel(model)
            category = None

            table_view.horizontalHeader().setStretchLastSection(True)
            table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table_view.setSelectionBehavior(QTableView.SelectRows)
            table_view.setSelectionMode(QTableView.SingleSelection)
            tab_widget.addTab(table_view, category)
        else:
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

                table_view.setStyleSheet(""" QHeaderView::section { border: 1px solid black; /* Adds border */  /* Makes text bold */ } QTableView QTableCornerButton::section { border: 0px; /* No border for corner button */ } QHeaderView::section:vertical { border: 0px; /* No border for row headers */ } """)

                # Adds the child widget QTableView to the QTabWidget. 
                # The tab is labeled with the category name.
                tab_widget.addTab(table_view, category)



class DateInputFilter(QObject):
    # Note that when Main Widget calls DateInputFilter it does it by DateInputFilter(self), the self is the instance of main widget
    # The main widget is now acting as the parent of DateInputFilter.
    # Establishes the parent-child relationship, allowing DateInputFilter to reference its parent widget if needed.
    def __init__(self, parent=None):
        super().__init__(parent)
        # Define the regular expression for the date format MM/DD/YYYY
        final_regex = QRegularExpression(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$")
        self.final_validator = QRegularExpressionValidator(final_regex, self) 

    # obj is the object that is being filtered for events. In your case, it refers to the QLineEdit widget 
    # (self.Create_Item_Date_Line_Edit) that the event filter is applied to.
    # self.Create_Item_Date_Line.installEventFilter(DateInput(self)) 
    # DateInputFilter intercepts and processes events for Create_Item_Date_Line_Edit.
    # "eventFiler()" is a function of Qt, and must be named exactly as that, cannot be named anything else. 
    # Override the eventFilter function, intercept events sent to obj and allows custom processing of those events.
    def eventFilter(self, obj, event):
        # Check if the type of the event is a key press event
        if event.type() == QEvent.KeyPress:
            # Retrieve the key code that is pressed, like Qt.Key_0 (IT DOES NOT GIVE the text of the key like "0")
            key = event.key()

            # Retrieves the current text from the object (i.e Create_Item_Date_Line_Edit), if pressed Qt.Key_0 then it's "0"
            # Retrieve what's currently in the object, could be "01" or "01/05"... 
            text = obj.text()

            # Retrieve the current cursor position within the text
            cursor_position = obj.cursorPosition()

            # Retrieve the text of the key pressed.
            char = event.text()

            # If the user input in date, but it's incorrect format and gets a red border, the user will likely delete 
            # the entire date to rewrite, in that case, the red border disappears. 
            # If the user only fix the portion that is incorrect, bringing back to the correct format, the red box will
            # Also disappear, because it's verified by the regex when FocusOut. 
            if len(text) == 0:
                obj.setStyleSheet("")
                group_box = obj.parent()
                create_button = group_box.findChild(QPushButton, 'Create_An_Item_Button')
                create_button.setEnabled(True)

            # This will allow backspaces and delete keys through, while blocking all letter keys
            if key in [Qt.Key_Backspace, Qt.Key_Delete, Qt.Key_Left, Qt.Key_Right]:
                return False

        
            # Check if the key pressed is a numeric key (0-9) -> only allows numeric inputs, no letters. 
            if Qt.Key_0 <= key <= Qt.Key_9:
                # Insert the character at the current cursor position
                new_text = text[:cursor_position] + char + text[cursor_position:]
                # After an input, the cursor position must move right, once, so update the cursor position +1.
                new_cursor_position = cursor_position + 1


                # Validate the new text -> as the user is typing in the date, restrict the users from being able to input
                # non-existence dates, like 13/34/2024 (no such thing as month 12 or days 34)
                if not self.is_valid_partial_date(new_text, new_cursor_position):
                    # If the result above is "if not False" = "if True", execute return True, which basically stops the eventFilter
                    # and does not update the with the new text, essentially ignoring the input, until it's in the correct allowable
                    # format, with valid months and days entry. 
                    return True  

                if new_cursor_position in [2, 5]:
                    # To handle correction when fully typed on a date, for example "12/30/2024"
                    # Lets say you want to change "12" to "10" -> visual: 10|/30/2024
                    # Len(new_text) > new_cursor_position = 12 > 2 = True
                    # new_text[2] != "/" -> "/" != "/" -> False
                    # If condition returns False and does not add in the "/", because it's already there. 
                    if len(new_text) > new_cursor_position and new_text[new_cursor_position] != "/":
                        new_text = new_text[:new_cursor_position] + "/" + new_text[new_cursor_position:]
                        new_cursor_position += 1
                    # Check if the length of the new_text is exactly equal to new_cursor_position. 
                    # This means that the cursor is at the end of the text, then we need to append a "/" at the end. 
                    elif len(new_text) == new_cursor_position:
                        new_text += "/"
                        new_cursor_position += 1
                
                # This will prevent the user from inputting more than 10 inputs, more than that and it will just ignores it.
                # MM/DD/YYYY = length of 10.
                if len(new_text) > 10:
                    return True
                
                # Update the new text and cursor position in the QLineEdit per the conditions met above. 
                obj.setText(new_text)
                obj.setCursorPosition(new_cursor_position)

                # Once the length is equal to 10, lose focus, so that it triggers FocusOut() and runs a final regex validator
                # To ensure the final form input from the user is valid MM/DD/YYYY. 
                if len(new_text) == 10:
                    obj.clearFocus()
                # if length !== 10, meaning user hasn't completed the input yet, so do not focus out. 
                return True
            return True
        
        # The FocusOut is for when the user finished typing in the date and clicks onto another QLineEdit, 
        # If the user input does not match the final_regex, return False, essentially keeping eventFIlter active to run
        # Until user input is correct -> see validate_final_input() for more details. 
        # Once user input is correct -> see validate_final_input() for more details. 
        elif event.type() == QEvent.FocusOut:
            self.validate_final_input(obj)
            return False
        
        return super().eventFilter(obj, event)
    
    # This function is to restrict the user form inputting in the month and dates that does not exist, like 13/50/2024.
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
    
    # This function is to perform a final regex validate to ensure the final form from user input is correct MM/DD/YYYY format.
    def validate_final_input(self, obj):
        text = obj.text()
        state, _, _ = self.final_validator.validate(text, len(text))
        group_box = obj.parent()
        create_button = group_box.findChild(QPushButton, 'Create_An_Item_Button')
        # only check once the user has completed the MM/DD/YYYY format, or at least put in 10 keystrokes
        if len(text) == 10:
            if state != QRegularExpressionValidator.Acceptable:
                # If failed regex, turn the create_button off so that user cannot input in wrong format date. 
                create_button.setEnabled(False)
                # Set red border for invalid input/format
                obj.setStyleSheet("QLineEdit {border: 2px solid red; }")
            else: 
                # If the user failed regex once and the button is off, this will turn the button back on once the user input
                # the correct format.
                create_button.setEnabled(True)
                # Reset to default style for valid input
                obj.setStyleSheet("QLineEdit {border:}")

        # if the lenght of text is less than 10, it means the user hasn't completed input before focusOut and should be flagged.
        elif len(text) < 10:
            create_button.setEnabled(False)
            obj.setStyleSheet("QLineEdit {border: 2px solid red; }")
    
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
        return 0 if self._data is None else len(self._data)
        
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

        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

        return None

    # Orientation: Can be either Qt.Horizontal for column headers or Qt.Vertical for row headers.
    # section: The section index of the header (i.e., the row or column number).
    # use headerData(), to provide header data, like titles of columns or rows, to the view.
    # user setHeaderDara(), to make the header editable during runtime [do not use in this case].
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._header[section]
        # if role == Qt.FontRole:
        #     font = QFont()
        #     font.setBold(True)
        #     return font
        return None # Use None to indicate no data for other roles



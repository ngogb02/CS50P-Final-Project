import pytest, os, io, sys
# use "." for Relative Imports or use "sys.path.append('C:\\Users\\ngogb\\OneDrive\\Documents\\Project\\CS50P-Final-Project\\QtDesigner')"
# Ensure the project directory is in sys.path
sys.path.append('C:\\Users\\ngogb\\OneDrive\\Documents\\Project\\CS50P-Final-Project\\QtDesigner')

from project import *
from contextlib import redirect_stdout

# This is a function that runs at the beginning of the test to clear any previously written contents in test_inventory.json
# and test_classes.py. 
def test_procedure():
    # clear test_inventory.json 
    with open("inventory.json", 'w') as file:
        file.write("")
    assert os.path.getsize("inventory.json") == 0

    # open test_classes.py and read all lines into variable lines
    with open("classes.py", 'r') as file:
        lines = file.readlines() #read all lines into a list

    # set the first line to first_line - keep the first line because it is an import function for class inheritance 
    first_line = lines[0]

    # write first_line to test_classes.py - all other content previously in test_classes.py gets overwritten/erased. 
    with open("classes.py", 'w') as file:
        file.write(first_line)

def test_create_item_class():
    # Create item Apple - 1st item
    create_item_class("Apple", "Fridge", 10, "12/04/2024")
    with open('classes.py', 'r') as file:
        content = file.read()

    expected_content = """
class Apple(InputReq):
    pass      
#create an instance of the new class
apple = Apple("Fridge", 10, "12/04/2024")
"""
    assert expected_content in content

    # Create item Banana - 2nd item
    create_item_class("Banana", "Fridge", 5, "12/06/2024")
    with open('classes.py', 'r') as file:
        content = file.read()

    expected_content = """
class Banana(InputReq):
    pass      
#create an instance of the new class
banana = Banana("Fridge", 5, "12/06/2024")
"""
    assert expected_content in content

    # Create item Mango - 3rd item
    create_item_class("Mango", "Fridge", 7, "12/10/2024")
    with open('classes.py', 'r') as file:
        content = file.read()

    expected_content = """
class Mango(InputReq):
    pass      
#create an instance of the new class
mango = Mango("Fridge", 7, "12/10/2024")
"""
    assert expected_content in content

def test_insert_item_into_inventory():
    insert_items_into_inventory("Fruits", "apple", "banana", "mango")

    # This is needed because a print function doesn't return anything, so can't assign the printed content to a variable
    # it needs to be captured and assigned to a variable, using the method below:
    output = io.StringIO() # Create a StringIO object to capture output
    with redirect_stdout(output): # Redirect standard output to the StringIO object (output)
        show_init_inventory() # Call the function, capturing its print output and putting it in object output by StringIO()
    content = output.getvalue() # Retrieve the captured output as a string

    expected_content = '''
Category: Fruits
 str --> apple
 str --> banana
 str --> mango
'''
    # Add .strip() to strip any leading and trailing whitespace 
    assert expected_content.strip() in content.strip()

def test_remove_items_from_inventory():
    # remove item by item from previous function that insert itms into inventory
    # remove apple
    remove_items_from_inventory("Fruits", "apple")
    output = io.StringIO() 
    with redirect_stdout(output): 
        show_init_inventory() 
    content = output.getvalue() 

    expected_content = '''
Category: Fruits
 str --> banana
 str --> mango
'''
    assert expected_content.strip() in content.strip()
    ######################################################################################
    # remove banana
    remove_items_from_inventory("Fruits", "banana")
    output = io.StringIO() 
    with redirect_stdout(output): 
        show_init_inventory() 
    content = output.getvalue() 

    expected_content = '''
Category: Fruits
 str --> mango
'''
    assert expected_content.strip() in content.strip()
    #######################################################################################
    # remove mango
    remove_items_from_inventory("Fruits", "mango")
    output = io.StringIO() 
    with redirect_stdout(output): 
        show_init_inventory() 
    content = output.getvalue() 

    expected_content = '''
Fruits
'''
    assert expected_content.strip() in content.strip()

    ########################################################################################
    # add all items back into inventory and remove them all at once.
    insert_items_into_inventory("Fruits", "apple", "banana", "mango")
    remove_items_from_inventory("Fruits", "apple", "banana", "mango")

    output = io.StringIO() 
    with redirect_stdout(output): 
        show_init_inventory() 
    content = output.getvalue() 

    expected_content = '''
Fruits
'''
    assert expected_content.strip() in content.strip()

def test_show_init_inventory():
    # This is just to show what's currntly in the inventory (this is not the json)
    # Since from the previous def, inventory was nothing but the category Fruits, show_init_inventory() will show just that.
    output = io.StringIO() 
    with redirect_stdout(output): 
        show_init_inventory() 
    content = output.getvalue() 

    expected_content = '''
Fruits
'''
    assert expected_content.strip() in content.strip()

def test_load_inventoryJSON():
    load_inventoryJSON('inventory.json')
    
def test_update_inventoryJSON():
    import importlib
    import classes
    importlib.reload(classes)
    from classes import apple, banana, mango
    insert_items_into_inventory("Fruits", apple, banana, mango)
    update_inventoryJSON("inventory.json")

    with open('inventory.json', 'r') as file:
        content = file.read()

    expected_content = """{
    "Fruits": {
        "Apple": {
            "_location": "Fridge",
            "_quantity": 10,
            "_date": "12/04/2024",
            "barcode": null,
            "price": null
        },
        "Banana": {
            "_location": "Fridge",
            "_quantity": 5,
            "_date": "12/06/2024",
            "barcode": null,
            "price": null
        },
        "Mango": {
            "_location": "Fridge",
            "_quantity": 7,
            "_date": "12/10/2024",
            "barcode": null,
            "price": null
        }
    }
}"""

    assert expected_content == content 

def test_save_inventoryJSON():
    inventory = {}
    save_inventoryJSON(inventory, 'inventory.json')

    with open("inventory.json", 'r') as file:
        content = file.read()
    
    expected_conent = "{}"

    assert expected_conent == content

def test_remove_item_from_JSON():
    
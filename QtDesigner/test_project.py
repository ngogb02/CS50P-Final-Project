import pytest, os
from icecream import ic
from project import create_item_class
from class_project import House
from classes import *


# This is a function that runs at the beginning of the test to clear any previously written contents in test_inventory.json
# and test_classes.py. 
def test_procedure():
    # clear test_inventory.json 
    with open("inventory.json", 'w') as file:
        file.write("")
    assert os.path.getsize("test_inventory.json") == 0

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

# def test_insert_items_into_inventory():
#     my_house = House()
#     insert_items_into_inventory("Fruits", "apple", "banana", "mango")

#     expected_content = """
#     {"Fruits": (apple, banana, mango)}
#     """

#     assert expected_content == my_house.inventory
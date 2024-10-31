from class_project import House, InputReq
from classes import *
from icecream import ic
from PySide6.QtWidgets import QApplication
from widget import Widget
import sys, json, os

my_house = House()

def create_item_class(item_name: str, location: str, quantity: int, date: str) -> None:
    with open('classes.py', 'r') as file:
        for line in file:
            if item_name in line:
                sys.exit("Item already exist!")
    class_builder = f"""
class {item_name.capitalize()}(InputReq):
    pass      
#create an instance of the new class
{item_name.lower()} = {item_name.capitalize()}("{location}", {quantity}, "{date}")
"""
    #append item class to classes.py 
    with open('classes.py', 'a') as file:
        file.write(class_builder)

def insert_items_into_inventory(Category: str, *item: object) -> None:
    my_house.add_item(Category, *item) 

def remove_items_from_inventory(Category: str, *item: object) -> None:
    my_house.remove_item(Category, *item) 

def show_init_inventory():
    print(my_house.print_inventory()) 

def load_inventoryJSON(filename):
        try:
            if os.path.getsize(filename) == 0:
                inventory = {} 
                with open(filename, 'w') as file:
                    json.dump(inventory, file)

                with open(filename, 'r') as file:
                    return json.load(file)
                
            else:
                with open(filename, "r") as file:
                    return json.load(file)
        except FileNotFoundError:
                return "File not found"

def update_inventoryJSON(filename):
    inventory = load_inventoryJSON(filename)

    for category, items in my_house.inventory.items():
        #if category already exist, and input None for items, will encounter error. 
        #if category does not exist and items is None, great a new category with an empty dict for adding items/attributes.
        if category not in inventory and (items is None or len(items) == 1):
            inventory[category] = {} 
        else:
            for item in items:
                if item is None:
                    sys.exit("You can't put None in inventory")
                else:
                #get class name and turn class atr into json serialization
                # try:
                    item_key = item.__class__.__name__
                    item_attr = item.__dict__
                # except AttributeError:
                # sys.exit("Cannot put None into existing category")
            #update the attributes that belongs to the key inside the category
                if category in inventory and item_key in inventory[category]:
                    inventory[category][item_key].update(item_attr)
                #if item class key is not inside category, make item class key and assign its attributes.
                elif category in inventory:
                    inventory[category][item_key] = item_attr
                else:
                    inventory[category] = {item_key: item_attr}
                            
    save_inventoryJSON(inventory, filename)

def save_inventoryJSON(inventory, filename):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent = 4)

def main():

    # insert_items_into_inventory("Fruits", apple, banana, mango)
    # create_item_class("strawberry", "Fridge", 69, "10/27/2024")
    # import classes, importlib
    # importlib.reload(classes)
    # from classes import strawberry
    # insert_items_into_inventory("Fruits", strawberry)
    # update_inventoryJSON("inventory.json")

    insert_items_into_inventory("Ingredients", None)
    update_inventoryJSON("inventory.json")


if __name__ == "__main__":
    main()
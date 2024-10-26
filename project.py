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

def show_inventory():
    print(my_house.print_inventory()) 

def load_inventory(filename):
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

def update_inventory(filename):
    inventory = load_inventory(filename)

    for category, items in my_house.inventory.items():
        for item in items:
            #get class name and turn class atr into json serialization
            item_key = item.__class__.__name__
            item_attr = item.__dict__
            #update the attributes that belongs to the key inside the category
            if category in inventory and item_key in inventory[category]:
                inventory[category][item_key].update(item_attr)
            #if item class key is not inside category, make item class key and assign its attributes.
            elif category in inventory:
                inventory[category][item_key] = item_attr
            else:
                inventory[category] = {item_key: item_attr}
                            
    save_inventory(inventory, filename)

def save_inventory(inventory, filename):
    with open(filename, "w") as file:
        json.dump(inventory, file, indent = 4)

def main():
    insert_items_into_inventory("Fruits", apple, banana, mango)
    show_inventory()
    update_inventory("inventory.json")
    
if __name__ == "__main__":
    main()

    # create_item_class("apple", "Fridge", 10, "10/10/2024")
    # create_item_class("banana", "Fridge", 6, "10/10/2024")
    # create_item_class("mango", "Fridge", 4, "10/08/2024" )

    # create_item_class("siracha", "Cabinet", 1, "05/15/2024")
    # create_item_class("soysauce", "Cabinet", 1, "08/18/2024")
    # create_item_class("cookingoil", "Cabinet", 3, "12/15/2023")
    # create_item_class("chickenbroth", "Cabinet", 10, "02/22/2024")
    # create_item_class("noodles", "Yellow box", 10, "07/15/2023")
    # create_item_class("veggies", "Fridge", 1, "10/15/2024")
    
    # create_item_class("snowboard", "Wall", 3, "05/22/2023")
    # create_item_class("jackets", "Yellow box", 1, "05/22/2023")
    # create_item_class("seasonpass", "Black stand", 1, "05/22/2023")

    # create_item_class("beef", "Fridge", 2, "10/15/2024")

    #ic(apple.quantity)
    #ic(apple.location)    
from class_project import House
from classes import *
from icecream import ic
import sys, json, os

my_house = House()

# This function writes to class.py file.
# Create a custom item class that inherits InputReq from class_project.py, 
# Then create that class object with the attributes input from user inputs.
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

def show_init_inventory() -> None:
    print(my_house.print_inventory()) 

def load_inventoryJSON(filename: str) -> None:
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

def update_inventoryJSON(filename: str) -> None:
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

def save_inventoryJSON(inventory: str, filename: str) -> None:
    with open(filename, "w") as file:
        json.dump(inventory, file, indent = 4)

def remove_item_from_JSON(filename: str, category: str, *items: object) -> None:
    #convert objects to their name
    item_names = [item.__class__.__name__ for item in items]

    #load JSON inventory 
    inventory = load_inventoryJSON(filename)

    #check if category is in dict, then check if item is in dict, if all true, remove/delete item from dict.
    #else, exit via ValueError. 
    if category in inventory:
        for item in item_names:
            if item in inventory[category]:
                del inventory[category][item]
            else:
                sys.exit(f"item: '{item}' does not exist in category: '{category}'")
    else:
        sys.exit(f"category: '{category}' does not exist in inventory")
        
    save_inventoryJSON(inventory, filename)

def remove_category_from_JSON(filename: str, category: str) -> None:
    inventory = load_inventoryJSON(filename)
    # try:
    if category in inventory:
        del inventory[category]
    else:
        sys.exit(f"category: '{category}' does not exist")
    # except KeyError as e:
    #     print(e)

    save_inventoryJSON(inventory, filename)

if __name__ == "__main__":
    main()
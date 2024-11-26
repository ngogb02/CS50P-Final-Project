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
        #if category does not exist and items is None, creat a new category with an empty dict for adding items/attributes.
        # if category not in inventory and (items is None or len(items) == 1):
        if category not in inventory and items is None:
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

    for item_name in item_names:
        if item_name == 'NoneType':
            return None
            print(f'item_name: {item_name}')
            print(f'items: {items}')

    #load JSON inventory 
    inventory = load_inventoryJSON(filename)

    #check if category is in dict, then check if item is in dict, if all true, remove/delete item from dict.
    #else, exit via ValueError. 
    if category in inventory:
        for item in item_names:
            if item in inventory[category]:
                del inventory[category][item]
            else:
                #sys.exit(f"item: '{item}' does not exist in category: '{category}'")
                return item
    else:
        #sys.exit(f"category: '{category}' does not exist in inventory")
        return category
        
    save_inventoryJSON(inventory, filename)

def remove_item_from_file(filename: str, item_name: str) -> None:
    with open(filename, 'r') as file:
        # lines is a list of lines read from the file
        lines = file.readlines()

    class_definition = f'class {item_name}'
    start_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith(class_definition):
            start_index = i
            break
    
    # If the class definition is found, remove the required lines
    if start_index is not None:
        del lines[start_index:start_index+4]

    # Write the updated content back to the file
    with open(filename, 'w') as file:
        file.writelines(lines)

def remove_category_from_JSON(filename: str, category: str) -> None:
    inventory = load_inventoryJSON(filename)

    if category in inventory:
        # For the category being deleted, look for all the items in that category and remove it from the classes.py file
        # So that when user goes to create same items in the same category, it will not conflict with creating_an_item func.
        items = inventory[category]
        class_filename = 'classes.py'
        for item in items:
            remove_item_from_file(class_filename, item)
        del inventory[category]
    else:
        # Returning False to trigger a warning messagebox by PySide6
        return False

    save_inventoryJSON(inventory, filename)

def main():
    #create_item_class("Apple", "Fridge", 10, "11/17/2024")
    # insert_items_into_inventory("Fruits", apple)
    # show_init_inventory()
    # update_inventoryJSON('inventory.json')
    #remove_item_from_file('classes.py', 'Banana')
    ...

if __name__ == "__main__":
    main()

# from class_project import InputReq

# class Apple(InputReq):
#     pass      
# #create an instance of the new class
# apple = Apple("Fridge", 40, "10/10/2023")

# class Banana(InputReq):
#     pass      
# #create an instance of the new class
# banana = Banana("Fridge", 56, "10/10/2024")

# class Mango(InputReq):
#     pass      
# #create an instance of the new class
# mango = Mango("Fridge456", 100, "10/08/2026")

# class Siracha(InputReq):
#     pass      
# #create an instance of the new class
# siracha = Siracha("Cabinet", 1, "05/15/2024")

# class Soysauce(InputReq):
#     pass      
# #create an instance of the new class
# soysauce = Soysauce("Cabinet", 1, "08/18/2024")

# class Cookingoil(InputReq):
#     pass      
# #create an instance of the new class
# cookingoil = Cookingoil("Cabinet", 3, "12/15/2023")

# class Chickenbroth(InputReq):
#     pass      
# #create an instance of the new class
# chickenbroth = Chickenbroth("Cabinet", 10, "02/22/2024")

# class Noodles(InputReq):
#     pass      
# #create an instance of the new class
# noodles = Noodles("Yellow box", 10, "07/15/2023")

# class Veggies(InputReq):
#     pass      
# #create an instance of the new class
# veggies = Veggies("Fridge", 1, "10/15/2024")

# class Snowboard(InputReq):
#     pass      
# #create an instance of the new class
# snowboard = Snowboard("Wall", 3, "05/22/2023")

# class Jackets(InputReq):
#     pass      
# #create an instance of the new class
# jackets = Jackets("Yellow box", 1, "05/22/2023")

# class Seasonpass(InputReq):
#     pass      
# #create an instance of the new class
# seasonpass = Seasonpass("Black stand", 1, "05/22/2023")

# class Beef(InputReq):
#     pass      
# #create an instance of the new class
# beef = Beef("Fridge", 2, "10/15/2024")

# class Strawberry(InputReq):
#     pass      
# #create an instance of the new class
# strawberry = Strawberry("Fridge", 20, "10/29/2024")

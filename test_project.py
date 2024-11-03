import pytest, os
from project import *
from classes import *
###IMPORTANT Note: DELETE EVERYTHING IN TEST_INVENTORY.JSON before running pytest test_project.py###
###the first function is to delete everything in the test_inventory.json file (elimnates doing it manually, or forgetting to do it)
def test_procedure():
    with open("test_inventory.json", 'w') as file:
        file.write("")
    assert os.path.getsize("test_inventory.json") == 0

def test_create_item_classes():
    #test_create_item_classes function checks if classes.py already contain the class/object before writing. 
    #this test will open classes.py, delete all lines except for import module, then perform funct and asserting.
    item_dict = {
    "Apple": {"location": "Fridge", "quantity": 40, "date": "10/10/2023"},
    "Banana": {"location": "Fridge", "quantity": 56, "date": "10/10/2024"},
    "Mango": {"location": "Fridge456", "quantity": 100, "date": "10/08/2026"},
    "Siracha": {"location": "Cabinet", "quantity": 1, "date": "05/15/2024"},
    "Soysauce": {"location": "Cabinet", "quantity": 1, "date": "08/18/2024"},
    "Cookingoil": {"location": "Cabinet", "quantity": 3, "date": "12/15/2023"},
    "Chickenbroth": {"location": "Cabinet", "quantity": 10, "date": "02/22/2024"},
    "Noodles": {"location": "Yellow box", "quantity": 10, "date": "07/15/2023"},
    "Veggies": {"location": "Fridge", "quantity": 1, "date": "10/15/2024"},
    "Snowboard": {"location": "Wall", "quantity": 3, "date": "05/22/2023"},
    "Jackets": {"location": "Yellow box", "quantity": 1, "date": "05/22/2023"},
    "Seasonpass": {"location": "Black stand", "quantity": 1, "date": "05/22/2023"},
    "Beef": {"location": "Fridge", "quantity": 2, "date": "10/15/2024"}
}
    with open("classes.py", 'r') as file:
        content = file.readlines()

    with open("classes.py", 'w') as file:
        file.write(content[0])

    for item, attributes in item_dict.items():

        location = attributes['location']
        quantity = attributes['quantity']
        date = attributes['date']
        create_item_class(item, location, quantity, date)
        with open("classes.py", 'r') as file:
            content = file.read()
        assert f"class {item.capitalize()}(InputReq):" in content
        assert f'{item.lower()} = {item.capitalize()}("{location}", {quantity}, "{date}")' in content

def test_insert_items_into_inventory():
    cat_item_dict ={
        "Fruits": [apple, banana, mango],
        "Ingredients": [siracha, soysauce, cookingoil, chickenbroth, noodles, veggies],
        "Snow Gear": [snowboard, jackets, seasonpass],
        "Meat": [beef]
    }
    for category, items in cat_item_dict.items():
        insert_items_into_inventory(category, *items)
        assert my_house.inventory[category] == items

    #re-initialize inventory to an empty dict for the next assert, otherwise, my_house.inventory from above carry over.
    my_house.inventory = {}
    insert_items_into_inventory("Fruits", apple, banana, mango)
    insert_items_into_inventory("Ingredients", siracha, soysauce, cookingoil, chickenbroth, noodles, veggies)
    insert_items_into_inventory("Snow Gear", snowboard, jackets, seasonpass)
    insert_items_into_inventory("Meat", beef)

    expected_dict = {
                    "Fruits": [apple, banana, mango],
                    "Ingredients": [siracha, soysauce, cookingoil, chickenbroth, noodles, veggies],
                    "Snow Gear": [snowboard, jackets, seasonpass],
                    "Meat": [beef]
                    }

    assert expected_dict == my_house.inventory

def test_remove_items_from_inventory():
    my_house.inventory = {}
    insert_items_into_inventory("Fruits", apple, banana, mango)

    # remove banana from dict
    remove_items_from_inventory("Fruits", banana)
    assert my_house.inventory == {"Fruits": [apple, mango]}

    #remove mango from dict
    remove_items_from_inventory("Fruits", mango)
    assert my_house.inventory == {"Fruits": [apple]}

    #insert more categories and remove item from last category, and middle category, middle item
    insert_items_into_inventory("Ingredients", siracha, soysauce, cookingoil, chickenbroth, noodles, veggies)
    insert_items_into_inventory("Snow Gear", snowboard, jackets, seasonpass)
    insert_items_into_inventory("Meat", beef)

    remove_items_from_inventory("Meat", beef)
    remove_items_from_inventory("Ingredients", cookingoil)
    assert my_house.inventory == {
                                "Fruits": [apple],
                                "Ingredients": [siracha, soysauce, chickenbroth, noodles, veggies],
                                "Snow Gear": [snowboard, jackets, seasonpass],
                                "Meat": [],
                                }

def test_show_init_inventory():
    my_house.inventory = {}
    insert_items_into_inventory("Fruits", apple, banana, mango)
    insert_items_into_inventory("Ingredients", siracha, soysauce, cookingoil, chickenbroth, noodles, veggies)
    insert_items_into_inventory("Snow Gear", snowboard, jackets, seasonpass)
    insert_items_into_inventory("Meat", beef)

    show_init_inventory() == f"""
                                Category: Fruits
                                Apple --> location: Fridge, quantity: 10, date: 10/10/2024
                                Banana --> location: Fridge, quantity: 6, date: 10/10/2024
                                Mango --> location: Fridge, quantity: 4, date: 10/08/2024
                                Category: Ingredients
                                Siracha --> location: Cabinet, quantity: 1, date: 05/15/2024
                                Soysauce --> location: Cabinet, quantity: 1, date: 08/18/2024
                                Cookingoil --> location: Cabinet, quantity: 3, date: 12/15/2023
                                Chickenbroth --> location: Cabinet, quantity: 10, date: 02/22/2024
                                Noodles --> location: Yellow box, quantity: 10, date: 07/15/2023
                                Veggies --> location: Fridge, quantity: 1, date: 10/15/2024
                                Category: Snow Gear
                                Snowboard --> location: Wall, quantity: 3, date: 05/22/2023
                                Jackets --> location: Yellow box, quantity: 1, date: 05/22/2023
                                Seasonpass --> location: Black stand, quantity: 1, date: 05/22/2023
                                Category: Meat
                                Beef --> location: Fridge, quantity: 2, date: 10/15/2024
                            """
    
def test_update_inventoryJSON():
    #to run this, ensure initial test_inventory.json is empty
    my_house.inventory = {}
    insert_items_into_inventory("Fruits", apple, banana, mango)
    update_inventoryJSON("test_inventory.json")

    with open('test_inventory.json', 'r') as file:
        try: 
            content = json.load(file)
        except json.JSONDecodeError:
            content = {}

    expected_json = {
    "Fruits": {
        "Apple": {
            "_location": "Fridge",
            "_quantity": 40,
            "_date": "10/10/2023",
            "barcode": None,
            "price": None
        },
        "Banana": {
            "_location": "Fridge",
            "_quantity": 56,
            "_date": "10/10/2024",
            "barcode": None,
            "price": None
        },
        "Mango": {
            "_location": "Fridge456",
            "_quantity": 100,
            "_date": "10/08/2026",
            "barcode": None,
            "price": None
        }
    }
}
    
    assert expected_json == content

    #create a new class item for category Fruits and insert it into json
    create_item_class("strawberry", "Fridge", 20, "10/29/2024")
    import classes, importlib
    importlib.reload(classes)
    from classes import strawberry
    insert_items_into_inventory("Fruits", strawberry)
    update_inventoryJSON("test_inventory.json")
    
    
    with open('test_inventory.json', 'r') as file:
            try: 
                content = json.load(file)
            except json.JSONDecodeError:
                content = {}
                
    expected_json = {
    "Fruits": {
        "Apple": {
            "_location": "Fridge",
            "_quantity": 40,
            "_date": "10/10/2023",
            "barcode": None,
            "price": None
        },
        "Banana": {
            "_location": "Fridge",
            "_quantity": 56,
            "_date": "10/10/2024",
            "barcode": None,
            "price": None
        },
        "Mango": {
            "_location": "Fridge456",
            "_quantity": 100,
            "_date": "10/08/2026",
            "barcode": None,
            "price": None
        },
        "Strawberry": {
            "_location": "Fridge",
            "_quantity": 20,
            "_date": "10/29/2024",
            "barcode": None,
            "price": None
        }
    }
}

    assert expected_json == content
    
    #update json with a new category but not put anything in.
    insert_items_into_inventory("Ingredients", None)
    update_inventoryJSON("test_inventory.json")
    
    with open('test_inventory.json', 'r') as file:
            try: 
                content = json.load(file)
            except json.JSONDecodeError:
                content = {}

    expected_content = {
    "Fruits": {
        "Apple": {
            "_location": "Fridge",
            "_quantity": 40,
            "_date": "10/10/2023",
            "barcode": None,
            "price": None
        },
        "Banana": {
            "_location": "Fridge",
            "_quantity": 56,
            "_date": "10/10/2024",
            "barcode": None,
            "price": None
        },
        "Mango": {
            "_location": "Fridge456",
            "_quantity": 100,
            "_date": "10/08/2026",
            "barcode": None,
            "price": None
        },
        "Strawberry": {
            "_location": "Fridge",
            "_quantity": 20,
            "_date": "10/29/2024",
            "barcode": None,
            "price": None
        }
    },
    "Ingredients": {}
}

    assert expected_content == content     

    #putting None into an existing category will trigger a sys.exit("You can't put None in inventory")
    with pytest.raises(SystemExit) as excinfo:
        insert_items_into_inventory("Ingredients", None)
        update_inventoryJSON("test_inventory.json")
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "You can't put None in inventory"

def test_remove_item_from_JSON():    
    #remove item from category in JSON file
    remove_item_from_JSON("test_inventory.json", "Fruits", strawberry, mango)
    with open("test_inventory.json", 'r') as file:
        inventory = json.load(file)

    expected_content = {
    "Fruits": {
        "Apple": {
            "_location": "Fridge",
            "_quantity": 40,
            "_date": "10/10/2023",
            "barcode": None,
            "price": None
        },
        "Banana": {
            "_location": "Fridge",
            "_quantity": 56,
            "_date": "10/10/2024",
            "barcode": None,
            "price": None
        }
    },
    "Ingredients": {}
}
    assert expected_content == inventory

    with pytest.raises(SystemExit) as excinfo:
        remove_item_from_JSON("test_inventory", "NotFruits", strawberry, mango)
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "category: 'NotFruits' does not exist in inventory"

def test_remove_category_in_JSON():
    #remove category in JSON file
    remove_category_from_JSON("test_inventory.json", "Fruits")
    inventory = load_inventoryJSON("test_inventory.json")

    expected_content = {
    "Ingredients": {}
}
    assert expected_content == inventory

    #remove a category that does not exist in JSON File
    with pytest.raises(SystemExit) as excinfo: 
        remove_category_from_JSON("test_inventory.json", "NotFruits") 
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "category: 'NotFruits' does not exist"
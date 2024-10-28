import pytest
from project import *


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


    
















    # item_list = [
    #     "Apple", "Fridge", 40, "10/10/2023"
    #     "Banana", "Fridge", 56, "10/10/2024"
    #     "Mango", "Fridge456", 100, "10/08/2026"
    #     "Siracha", "Cabinet", 1, "05/15/2024"
    #     "Soysauce", "Cabinet", 1, "08/18/2024"
    #     "Cookingoil", "Cabinet", 3, "12/15/2023"
    #     "Chickenbroth", "Cabinet", 10, "02/22/2024"
    #     "Noodles", "Yellow box", 10, "07/15/2023"
    #     "Veggies", "Fridge", 1, "10/15/2024"
    #     "Snowboard", "Wall", 3, "05/22/2023"
    #     "Jackets", "Yellow box", 1, "05/22/2023"
    #     "Seasonpass", "Black stand", 1, "05/22/2023"
    #     "Beef", "Fridge", 2, "10/15/2024"
    # ]
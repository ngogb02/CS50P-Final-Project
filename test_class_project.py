import pytest, warnings
from class_project import House, Apple, Banana, Strawberry, Vegetable, Sriracha, SoySauce, CookingOil, ChickenBroth, Noodles, Snowboard, Jackets, SeasonPass, Beef

#check print_inventory_in_House
def test_print_inventory_in_House():
    my_house = House()
    apple = Apple("Fridge", 10, "10/15/2024")
    banana = Banana("Fridge", 6, "10/10/2024")
    strawberry = Strawberry("Fridge", 16, "10/08/2024")
    sriracha = Sriracha("Cabinet", 1, "05/15/2024")
    soysauce = SoySauce("Cabinet", 1, "08/18/2024")
    cooking_oil = CookingOil("Cabinet", 3, "12/15/2023")
    chicken_broth = ChickenBroth("Cabinet", 10, "02/22/2024")
    snowboard = Snowboard("Wall", 3, "05/22/2023")
    jackets = Jackets("Yellow box", 1, "05/22/2023")
    season_pass = SeasonPass("Black stand", 1, "05/22/2023")
    beef = Beef("Fridge", 2, "10/15/2024")
    noodle = Noodles("Yellow box", 10, "07/15/2023")
    veggie = Vegetable("Fridge", 1, "10/15/2024")

    my_house.add_item("Fruit", apple, banana, strawberry, veggie)
    my_house.add_item("Ingredients", sriracha, soysauce, cooking_oil, chicken_broth, noodle)
    my_house.add_item("Meat", beef)
    my_house.add_item("SnowGear", snowboard, jackets, season_pass)

    assert my_house.inventory == {"Fruit": [apple, banana, strawberry, veggie],
                                  "Ingredients": [sriracha, soysauce, cooking_oil, chicken_broth, noodle],
                                  "Meat": [beef],
                                  "SnowGear": [snowboard, jackets, season_pass]
                                }
    #checking method add and consume works for variables inside my_house.inventory
    apple.consume(5)
    assert my_house.inventory["Fruit"][0].quantity == 5
    apple.add(6)
    assert my_house.inventory["Fruit"][0].quantity == 11
    noodle.consume(5)
    assert my_house.inventory["Ingredients"][4].quantity == 5
    noodle.add(6)
    assert my_house.inventory["Ingredients"][4].quantity == 11

#check remove_item_in_House
@pytest.mark.parametrize("category", ["SnowGear", "Yellow box"])
def test_remove_item_in_House(category):
    apple = Apple("Fridge", 10, "10/15/2024")
    my_house = House()
    my_house.add_item("Fruit", apple)
    with pytest.raises(SystemExit) as excinfo:
        my_house.remove_item(category, apple)
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "You must pick an existing category"

    with pytest.raises(SystemExit) as excinfo:
        banana = Banana()
        my_house.remove_item("Fruit", banana)
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "Item does not exist"

#check add_item in House
@pytest.mark.parametrize("category", [10.0, 10, 0, -1, -1.0, None])
def test_add_item_in_House(category):
    apple = Apple("Fridge", 10, "10/15/2024")
    with pytest.raises(SystemExit) as excinfo:
        House.add_item(category, apple)
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "Category must be a str"

#check date to be a str
@pytest.mark.parametrize("date", [10, 10.0, 0, 1, -1, -2, -2.0])
def test__init_type_check_date(date):
    with pytest.raises(SystemExit) as excinfo:
        apple = Apple(date = date)
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "Date input must be a string"

#check date to be in the correct format mm/dd/yyyy
@pytest.mark.parametrize("date", ["02-20-1996", "02_20_1996", "02 20 1996", "02201996"])
def test__init_type_check_date(date):
    with pytest.raises(SystemExit) as excinfo:
        apple = Apple(date = date)
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "Date must be input as dd/mm/yyyy format"

#check date input as intented
def test_date():
    apple = Apple(date = None)
    assert apple.date == None
    apple.date = "02/20/1996"
    assert apple.date == "02/20/1996"

#check location to be a str
@pytest.mark.parametrize("location", [10.0, 10, 0, -1, -2])
def test__init_type_check_loc(location):
    with pytest.raises(SystemExit) as excinfo:
        apple = Apple(location = location)
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "Location input must be a string"

    #check location atr is functioning as intended
    apple = Apple(location = "Fridge")
    assert apple.location == "Fridge"
    apple.location = "Box"
    assert apple.location == "Box"
    apple.location = None
    assert apple.location == None

#check quantity to be an int
@pytest.mark.parametrize("quantity", [10.0, "str"])
def test_init_type_check_qty(quantity):
    with pytest.raises(SystemExit) as excinfo:
        apple = Apple(quantity = quantity)
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "Quantity input must be an int"


def test_init():
    #check instance with some argument inputs, not all
    apple = Apple("fridge", 10, "10/15/2024")
    assert apple.location == "fridge"
    assert apple.quantity == 10
    assert apple.price == None
    assert apple.date == "10/15/2024"
    assert apple.barcode == None

    #check instance without any argument inputs
    apple = Apple()
    assert apple.location == None
    assert apple.quantity == None
    assert apple.price == None
    assert apple.date == None
    assert apple.barcode == None

def test_class_apple_superclass_fruit_add_method():
    #check attribute quantity when instance of quantity = 10
    apple = Apple(quantity = 10)
    assert apple.location == None
    assert apple.quantity == 10
    assert apple.price == None
    assert apple.date == None
    assert apple.barcode == None

    #adding
    apple.add(10)
    assert apple.quantity == 20
    apple.add(10)
    assert apple.quantity == 30
    apple.add(0)
    assert apple.quantity == 30

    #raise SystemExit message for adding negative value
    with pytest.raises(SystemExit) as excinfo:
        apple.add(-10)
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "ValueError: Cannot add a negative amount"

def test_class_apple_superclass_fruit_consume_method():
    #consuming
    apple = Apple(quantity = 10)
    assert apple.quantity == 10
    apple.consume(5)
    assert apple.quantity == 5
    apple.consume(0)
    assert apple.quantity == 5
    apple.consume(5)
    assert apple.quantity == 0

    #raise SystemExit message for consuming negative value
    with pytest.raises(SystemExit) as excinfo:
        apple.consume(-10)
    assert excinfo.type == SystemExit
    assert excinfo.value.code == "Cannot consume a negative amount"

    #raise Warning message for consuming more than exist
    apple.add(10)
    with pytest.warns(UserWarning, match="This is more than exist, it will consume the entire stock"):
        apple.consume(100)
    assert apple.quantity == 0




import warnings, sys, re
from icecream import ic
# function/class guidelines:
# 1. Short and concise
# 2. Specify return type
# 3. Make as simple and reusable as possible
# 4. Document all your functions
# 5. Handle errors appropriately
# system requirement:
# 6. Establish Reorder Point (if quantity < #, send message “hey, we’re running out of this!”

class House():
    def __init__(self) -> None:
        self.inventory = {}

    def add_item(self, category: str, *item) -> None:
        if not isinstance(category, str):
            sys.exit("Category must be a str")
        elif category not in self.inventory:
            self.inventory[category] = []
        for item in item:
            self.inventory[category].append(item)

    def remove_item(self, category: str, item) -> None:
        if category not in self.inventory:
            sys.exit("You must pick an existing category")
        elif category in self.inventory and item in self.inventory[category]:
            self.inventory[category].remove(item)
        else:
            sys.exit("Item does not exist")

    def print_inventory(self):
        result = []
        for key, obj_list in self.inventory.items():
            result.append(f"Category: {key}")
            for obj in obj_list:
                class_name = obj.__class__.__name__
                result.append(f" {class_name} --> {obj}")
        return "\n".join(result)


class InputReq():
    def __init__(self, location: str = None, quantity: int = None, date: str = None, price: float = None, barcode: int = None) -> None:
        self.location = location
        self.quantity = quantity
        self.date = date
        self.barcode = barcode #-> concept for next iteration, for now stays as None :)
        self.price = price     #-> concept for next iteration, for now stays as None :)

    def __str__(self):
        return f"location: {self.location}, quantity: {self.quantity}, date: {self.date}"

    #Setter/Getter of date
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date: str) -> None:
        if date is None:
            self._date = None
        elif not isinstance(date, str):
            sys.exit("Date input must be a string")
        elif matches := re.search(r"^^\b(0[1-9]|1[0-2])/([0-2][0-9]|3[0-1])/(\d{4})\b$", date, re.IGNORECASE):
            self._date = matches.group()
        else:
            sys.exit("Date must be input as dd/mm/yyyy format")

    #Setter/Getter of location
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: str) -> None:
        if location is None:
            pass
        elif not isinstance(location, str):
            sys.exit("Location input must be a string")

        self._location = location

    #Setter/Getter of quanity
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        if quantity is None:
            pass
        elif not isinstance(quantity, int):
            sys.exit("Quantity input must be an int")
        elif quantity <= 0:
            warnings.warn("The initiated quantity is 0, are you sure?", UserWarning, stacklevel=5)

        self._quantity = quantity


    #adding for quantity increase
    def add(self, _: int):
        if _ < 0:
            sys.exit("ValueError: Cannot add a negative amount")

        self._quantity += _

    #consuming for quantity decrease
    def consume(self, _: int):
        if _ < 0:
            sys.exit("Cannot consume a negative amount")
        elif _ > self.quantity:
            warnings.warn("This is more than exist, it will consume the entire stock", UserWarning, stacklevel=4)

        self._quantity -= _
        self._quantity = max(0, self.quantity)

class Apple(InputReq):
    pass

class Banana(InputReq):
    pass

class Strawberry(InputReq):
    pass

class CookingOil(InputReq):
    pass

class Sriracha(InputReq):
    pass

class SoySauce(InputReq):
    pass

class Noodles(InputReq):
    pass

class Beef(InputReq):
    pass

class ChickenBroth(InputReq):
    pass

class Vegetable(InputReq):
    pass

class Snowboard(InputReq):
    pass

class Jackets(InputReq):
    pass

class SeasonPass(InputReq):
    pass

def main():
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

     ic(my_house.print_inventory())
     #print(my_house.print_inventory())

     apple.consume(5)
     ic(my_house.print_inventory())


if __name__ == "__main__":
    main()



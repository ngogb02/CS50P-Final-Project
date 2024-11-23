import warnings, sys, re
from icecream import ic

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

    def remove_item(self, category: str, *item) -> None:
        if category not in self.inventory:
            sys.exit("You must pick an existing category")
        for item in item:
            if category in self.inventory and item in self.inventory[category]:
                self.inventory[category].remove(item)
            else:
                sys.exit(f"{item.__class__.__name__.lower()} does not exist")

    def print_inventory(self):
        result = []
        for key, obj_list in self.inventory.items():
            if obj_list is None or all(item is None for item in obj_list):
                result.append(f"{key}")
            else:
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


if __name__ == "__main__":
    main()


